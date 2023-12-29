const server = 'https://api.artifactsmmo.com';
const token = 'YOUR_TOKEN_HERE';
const character = 'CHARACTER_NAME_HERE';
let cooldown = 5;
let interval;

function performGathering() {
  const url = `${server}/my/${character}/action/gathering`;

  const headers = {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    Authorization: `Bearer ${token}`,
  };

  return fetch(url, {
    method: 'POST',
    headers: headers,
  }).then((gatheringResponse) => {
    if (gatheringResponse.status === 498) {
      console.log('The character cannot be found on your account.');
       document.write("The character cannot be found on your account.");
      clearInterval(interval);
      
      return;
    }

    if (gatheringResponse.status === 497) {
      console.log("Your character's inventory is full.");
      document.write("Your character's inventory is full.");
      clearInterval(interval);
      return;
    }

    if (gatheringResponse.status === 499) {
      console.log('Your character is in cooldown.');
      document.write('Your character is in cooldown.');
      clearInterval(interval);
      return;
    }

    if (gatheringResponse.status === 496) {
      console.log('The resource is too high-level for your character.');
       document.write('The resource is too high-level for your character.');
      clearInterval(interval);
      return;
    }

    if (gatheringResponse.status !== 200) {
      console.log('An error occurred while gathering the resource.');
      document.write('An error occurred while gathering the resource.');

      clearInterval(interval);
      return;
    }

    if (gatheringResponse.status === 200) {
      return gatheringResponse.json().then((data) => {
        console.log('Your character successfully gathered the resource.');
        document.write('Your character successfully gathered the resource.');
        cooldown = data.data.cooldown.totalSeconds;
      });
    }
  });
}

// Loop
function main() {
  interval = setInterval(() => {
    performGathering()
  }, cooldown * 1000);
}

main();