# 🎮 Tic-Tac-Toe Game in C

## 📌 About the Project

This project consists of developing a **Tic-Tac-Toe game using the C programming language**, executed directly in the terminal.

The game allows two players to participate in the same match, taking turns playing with the symbols **X** and **O** on a 3x3 game board.

The program uses matrices, loops, and conditional statements to manage player moves and update the board throughout the game.

## ⚙️ Features

- 3x3 game board.
- Two players: X and O.
- Alternating turns between players.
- Row and column selection to make moves.
- Validation of already occupied positions.
- Board updates and display after each move.
- Automatic game termination when all nine positions are filled.

## 🛠️ Technologies Used

- **C Language:** Game logic development.
- **`stdio.h` Library:** Input and output operations.
- **Arrays (Matrices):** Storage of board positions.
- **Conditional Statements:** Move control.
- **Loops (`for` and `while`):** Board initialization, game execution, and control.

## 🧠 Programming Concepts Applied

The following programming concepts were used during development:

| Concept | Application |
|---|---|
| Variables | Store rows, columns, and the number of moves. |
| Matrices | Represent the 3x3 game board. |
| `for` | Initialize and display the board. |
| `while` | Control turns and validate positions. |
| `if/else` | Check whether positions are available. |
| `scanf()` | Receive player input. |
| `printf()` | Display messages and the game board. |

## ▶️ How to Run the Project

### 1. Prerequisites

You need a C compiler installed, such as GCC.

### 2. Clone the Repository

```bash
git clone REPOSITORY_URL
```

### 3. Navigate to the Project Folder

```bash
cd FOLDER_NAME
```

### 4. Compile the Program

```bash
gcc "Jogo da veia.c" -o game
```

### 5. Run the Program

On Linux:

```bash
./game
```

On Windows:

```bash
game.exe
```

## 🎲 Execution Example

```text
PLAYER 'X' TURN

Enter the row (0, 1 or 2): 0
Enter the column (0, 1 or 2): 0

Board
 X  -  -
 -  -  -
 -  -  -

PLAYER 'O' TURN

Enter the row (0, 1 or 2): 1
Enter the column (0, 1 or 2): 1

Board
 X  -  -
 -  O  -
 -  -  -
```

## 🚀 Possible Future Improvements

- Implement victory detection across rows, columns, and diagonals.
- Display a message identifying the winning player.
- Implement draw detection.
- Add validation to prevent coordinates outside the board boundaries.
- Improve the terminal user interface.

## 🎯 Academic Purpose

The objective of this project is to develop and improve programming logic and C language skills by applying fundamental concepts such as matrices, conditional statements, loops, and data manipulation.

This exercise also provides an introduction to game development using structured programming.

---

**Project developed for academic purposes and learning the C programming language.**
