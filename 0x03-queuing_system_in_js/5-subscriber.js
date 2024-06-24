const redis = require("redis");

const subscriber = redis.createClient();

subscriber.on("connect", function() {
  console.log("Redis client connected to the server");
});

subscriber.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

subscriber.subscribe("holberton school channel");

subscriber.on("message", function(channel, message) {
  console.log(message);

  if (message === "KILL_SERVER") {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
