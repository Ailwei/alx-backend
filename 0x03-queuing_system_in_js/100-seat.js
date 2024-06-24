const express = require('express');
const redis = require('redis');
const Queue = require('bull');
const { promisify } = require('util');

const app = express();
const port = 1245;

const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

let availableSeats = 50;
let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync('available_seats', number.toString());
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats) || 0;
}

const queue = new Queue('reserve_seat');

queue.process(async (job) => {
  const currentSeats = await getCurrentAvailableSeats();

  if (currentSeats === 0) {
    reservationEnabled = false;
    throw new Error('Not enough seats available');
  } else {
    await reserveSeat(currentSeats - 1);
    if (currentSeats === 1) {
      reservationEnabled = false;
    }
  }
});

app.use(express.json());

app.get('/available_seats', (req, res) => {
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = await queue.add({});
  job.on('completed', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });

  res.json({ status: 'Reservation in process' });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  await queue.add({});
  await queue.close();

  if (availableSeats === 0) {
    reservationEnabled = false;
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
