import { createClient, print } from 'redis';

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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value).then((res) => console.log(`Reply: ${res}`));
};

function displaySchoolValue(schoolName) {
  client.get(schoolName).then((res) => console.log(res));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

