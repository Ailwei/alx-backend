const redis = require("redis");

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

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(error, result) {
    if (error) {
      console.error(error);
      throw error;
    }
    console.log(result);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
