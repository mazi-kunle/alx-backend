import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('ready', () => {
  console.log('Redis client connected to the server');
});

(async () => {
  await client.connect();
})();

const subscriber = client.duplicate();
subscriber.on('error', err => console.error(err));
subscriber.connect();

subscriber.subscribe('holberton school channel', (message, channel) => {
  console.log(message);

  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    process.exit(0);
  }
});