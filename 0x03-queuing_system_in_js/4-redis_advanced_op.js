import { createClient  } from "redis";

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

(async () => {
  await client.HSET('HolbertonSchools', 'Portland', 50).then((res) => console.log(`Reply: ${res}`));
  await client.HSET('HolbertonSchools', 'Seattle', 80).then((res) => console.log(`Reply: ${res}`));
  await client.HSET('HolbertonSchools', 'New York', 20).then((res) => console.log(`Reply: ${res}`));
  await client.HSET('HolbertonSchools', 'Bogota', 20).then((res) => console.log(`Reply: ${res}`));
  await client.HSET('HolbertonSchools', 'Cali', 40).then((res) => console.log(`Reply: ${res}`));
  await client.HSET('HolbertonSchools', 'Paris', 2).then((res) => console.log(`Reply: ${res}`));

  await client.HGETALL('HolbertonSchools').then((res) => console.log(res));
})();

