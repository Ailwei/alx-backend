const redis = require("redis");
const { promisify } = require("util");

const client = redis.createClient();

client
  .on("connect", function() {
    console.log("Redis client connected to the server");
  })
  .on("error", function(error) {
    console.error(`Redis client not connected to the server: ${error}`);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const asyncGet = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const res = await asyncGet(schoolName);
    console.log(res);
  } catch (error) {
    console.error(error);
    throw error;
  }
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
