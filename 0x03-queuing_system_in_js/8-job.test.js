const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs function', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  test('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'Message 1' },
      { phoneNumber: '4153518781', message: 'Message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).toBe(jobs.length);

    jobs.forEach((jobData, index) => {
      const job = queue.testMode.jobs[index];
      expect(job.type).toBe('push_notification_code_3');
      expect(job.data).toEqual(jobData);
    });
  });
});
