# Devblog: New Mechanics & Sandwhisper

This devblog covers update **5.1**, coming in August, and introduces two major new systems:

- A new map system with pathfinding and a layer-based world structure  
- Multi-character combat on the same account

Rolling out such big changes mid-season might seem unusual, but it will allow me to analyze player comprehension and balance these mechanics before deploying them across the full game.

These systems will be fully leveraged on **Sandwhisper Isle** and will be rolled out across the game world in the next season. So don't worry about your bots — everything should continue working the same on current content.

But before diving into Sandwhisper, let's take a look at the two new gameplay mechanics.

---

## Map System

One of the big upcoming changes is the complete rework of the map system. This will bring major changes to how you navigate in **Artifacts**.

---

### 1. Goodbye Rectangular Maps, Welcome Pathfinding (A*)!

Maps now have an `access` property, making the world more coherent: with water, mountains, and obstacles. Not all maps will be accessible anymore.

Some maps will require teleportation (via potion), while others will have specific conditions — such as owning an item or reaching a certain level.

**Added to the `MapSchema` model:**
```json
"access": {
  "type": "standard/blocked/conditional/teleport_required",
  "conditions": []
}
```

Logs and responses will now include the path your character used, helping you optimize travel.

---

### 2. A World Made of Layers!

![layers](https://i.imgur.com/90m8D8T.gif)

The world is now made up of **three layers**:

- `interior`  
- `overworld`  
- `underground`

Characters using the `Move` endpoint will move within a single layer. But they can now **transition between layers** using the new endpoint:  
`/my/{character}/action/transition` — with the help of potions or items.

**Example map object:**
```json
{
  "data": {
    "map_id": 1231,
    "name": "Sandwhisper Isle",
    "skin": "desertisland_10",
    "x": -3,
    "y": 19,
    "layer": "overworld",
    "content": {
      "type": "monster",
      "code": "sandwarden"
    },
    "access": {
      "type": "standard",
      "conditions": []
    },
    "transition": {
      "map_id": 1233,
      "x": -3,
      "y": 19,
      "layer": "interior",
      "cost": {
        "gold": null,
        "items": [
          {
            "code": "sandwhisper_key",
            "quantity": 1
          }
        ]
      }
    }
  }
}
```

These changes introduce a **map ID**, which uniquely identifies each map — since different layers can share the same coordinates.  
The existing endpoints will remain compatible with coordinates, now with layer precision, and new endpoints will also support map IDs.

This is a **big transition**, but I’m really excited to introduce it.  
While only the new zone will benefit from it initially in 5.1, the rest of the game world will be updated progressively.

---

## Multi-Character Combat

One of the most requested features is finally coming: **multi-character combat**, arriving with update **5.1**!

This required several fundamental changes to the combat system.

---

### Changes to the Combat System

Gone are the days of your character always starting first. Introducing a new stat: **initiative** — determining turn order between characters and monsters.

> *All existing monsters will have zero initiative and still act second (as they do now). Their stats will only be updated next season to avoid breaking current scripts.*

A second new stat is also introduced: **threat** — relevant only for multi-character battles, as it affects which character the monster is likely to attack.

---

### Monster Types

Monsters now fall into three categories:

- `normal`  
- `elite`: Stronger than normal monsters of the same level, protecting rare resources (e.g., Lich, Rosenblood)  
- `boss`: The only monsters that can be fought in groups

---

### How Multi-Character Combat Works

Group battles are as simple as regular ones:  
All characters must be on the monster’s map. A new endpoint allows you to specify which characters will join the fight. You can engage with **up to 3 or 4** characters from your account.

> *The feature is still in development, and the final limit on the number of characters in a fight hasn’t been confirmed yet.*

Since the system is still actively being developed, I’ll wait before diving into the details of equipment, runes, or utilities — but there will be **boss-focused content** with mechanics giving specific **roles** to your characters.

---

## Sandwhisper Isle

![Logo](https://i.imgur.com/5fRjfZt.png)

**Sandwhisper Isle** is the new zone for characters **level 40 to 50**.  
It includes **new resources**, **five new monsters** (including **two group bosses**), and is the **first zone to use the new map system**.

![island](https://i.imgur.com/K19j71Y.png)  
![island](https://i.imgur.com/Yj2Roj9.png)  
![layer](https://i.imgur.com/MEWeqUS.png)

The island will cost **1000 gold per trip**, so you might want to find a way to access its bank.  
Apparently, you’ll need to **earn its trust** before they’ll let you in...

Too many pirates have been trying to loot the island...

---

For now, I’ll stop here and let you discover the **bosses and secrets** of this mysterious new island.  
See you in **August**!

Thanks,  
**muigetsu**
