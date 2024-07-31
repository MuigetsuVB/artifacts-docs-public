const server = "https://api.artifactsmmo.com";
const token =
  "YOUR_TOKEN"; // Remplacez par votre token
const character = "CHARACTER_NAME"; // Replace with your character's name

let cooldown;
let state = "gathering";

//position of the resource to be gathered
const x = -1;
const y = 0;

const headers = {
  "Content-Type": "application/json",
  Accept: "application/json",
  Authorization: `Bearer ${token}`,
};

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function loop() {
  if (state == "gathering") {
    performGathering();
  } else if (state == "bank") {
    prepareDeposit();
  }
}

function performGathering() {
  const url = `${server}/my/${character}/action/gathering`;

  fetch(url, { method: "POST", headers: headers }).then((gatheringResponse) => {
    if (gatheringResponse.status === 497) {
      // Inventory full
      state = "bank";
      moveTo(4, 1); // Move to the bank
    } else if (gatheringResponse.status === 499) {
      console.log("Character in cooldown. Retry in 5 seconds.");
      setTimeout(loop, 5 * 1000);
    } else if (gatheringResponse.status === 200) {
      state = "gathering";
      gatheringResponse.json().then((data) => {
        console.log("Your character has successfully gathering the resource.");
        cooldown = data.data.cooldown.total_seconds;
        setTimeout(loop, cooldown * 1000); // Wait for cooldown to end
      });
    } else {
      state = "gathering";
      moveTo(x, y);
    }
  });
}

function moveTo(mx, my) {
  const moveUrl = `${server}/my/${character}/action/move`;
  const moveData = { x: mx, y: my };

  fetch(moveUrl, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(moveData),
  }).then((moveResponse) => {
    if (moveResponse.status === 200) {
      moveResponse.json().then((data) => {
        console.log("Successful move.");
        setTimeout(loop, data.data.cooldown.total_seconds * 1000); // Wait for cooldown to end
      });
    } else {
      console.log("Error when moving.");
    }
  });
}

function prepareDeposit() {
  const url = `${server}/characters/${character}`;
  const headers = {
    Accept: "application/json",
    Authorization: `Bearer ${token}`,
  };

  fetch(url, { method: "GET", headers: headers }).then((infoResponse) => {
    if (infoResponse.status === 200) {
      infoResponse.json().then((data) => {
        depositAllItems(data.data); // Deposit all inventory items
      });
    } else {
      console.log("Error retrieving character information.");
    }
  });
}

async function depositAllItems(characterData) {
  for (let i = 1; i <= 20; i++) {
    const slot = `inventory_slot${i}`;
    const quantity = `inventory_slot${i}_quantity`;

    if (characterData[slot] && characterData[quantity] > 0) {
      depositItem(characterData[slot], characterData[quantity]);
      await delay(3000); //wait for the deposit cooldown time
    }
  }
  state = "gathering";
  loop();
}

function depositItem(itemCode, quantity) {
  const depositUrl = `${server}/my/${character}/action/bank/deposit`;
  const itemData = { code: itemCode, quantity: quantity };

  fetch(depositUrl, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(itemData),
  }).then((depositResponse) => {
    if (depositResponse.status === 200) {
      depositResponse.json().then((data) => {
        console.log(`Item ${itemCode} successfully deposited.`);
      });
    } else {
      console.log(`Error when depositing item ${itemCode}.`);
    }
  });
}

loop();
