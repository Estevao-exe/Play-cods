# 🗑️ Battle in the Junkyard

A simple text-based battle game made in Python, where you face the fearsome **Trash Bot** in a junkyard!

## 🎮 About the Game

You are in the junkyard and encountered a **Trash Bot**. Now you must defeat it in up to 5 rounds!

- **Your starting life:** 70
- **Trash Bot's life:** 50
- **Potions available:** 1

## 🕹️ How to Play

When the game starts, enter your character's name.

Each round you can choose:

| Option | Action       | Effect                                      |
|--------|--------------|---------------------------------------------|
| `1`    | Attack       | Deals **25** damage to the Trash Bot        |
| `2`    | Use Potion   | Restores **15** life (only 1 potion)        |
| `3`    | Flee         | (Not yet implemented)                       |

⚠️ **Warning:** After you attack, the Trash Bot counterattacks and deals **15** damage!

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Download or clone this repository.
3. Open the terminal in the project folder and run:


📜 Rules

The game lasts a maximum of 5 rounds.
If the Trash Bot's life reaches 0 or less → YOU WIN!
If the Trash Bot's life is still positive after 5 rounds → GAME OVER!
You can only use the potion once.

battle-in-the-junkyard/
├── battle_in_the_junkyard.py   # Main game code
└── README.md                   # This file
🛠️ Future Improvements (Suggestions)

 Implement the flee action
 Add more enemy types
 Scoring system
 Critical hit chance on attacks
 More potions or special items


Made with ❤️ in Python

Good luck in the junkyard, warrior! 🗑️⚔️
```bash
python battle_in_the_junkyard.py
