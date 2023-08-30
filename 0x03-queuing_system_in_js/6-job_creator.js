import kue from 'kue';

const queue = kue.createQueue();
const obj = {
  phoneNumber: '128945',
  message: 'This is a message',
};

const job = queue.create('push_notification_code', obj)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
