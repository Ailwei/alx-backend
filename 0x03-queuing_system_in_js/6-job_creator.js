const kue = require('kue');
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '+1234567890',
  message: 'This is a test notification message',
};

const job = queue.create('push_notification_code', jobData)
  .save(function(err) {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', function() {
  console.log('Notification job completed');
});

job.on('failed', function() {
  console.log('Notification job failed');
});
