#  Python Cricket Game (You vs Computer)

A fun **console-based Hand Cricket game** built using Python where you play against the computer. The game simulates real cricket concepts like **overs, wickets, toss, batting, bowling, and chasing targets**.

---

## Features

- Toss system (Heads/Tails)
- Choose to **bat or bowl first**
- Supports **multiple overs & players**
- Real-time score updates
- Proper win/loss/draw result handling
- Input validation to avoid crashes

---

## Tech Stack

- **Language:** Python 3
- **Library Used:** `random`
- **Platform:** Terminal / Command Prompt

---

## How the Game Works

### 1️. Toss
- User chooses **Heads or Tails**
- Winner decides to **bat or bowl first**

### 2️. Batting & Bowling Logic
- User enters a number between **0–6**
- Computer randomly selects a number
- If both numbers match → **OUT**
- Otherwise → runs are added

### 3️. Match Result
- Team scoring **target runs** first wins
- All out before chasing target → loss
- Equal scores → draw

---

## How to Run the Game

### Step 1: Clone the Repository
```bash
git clone https://github.com/shivam183-star/Play-Cricket-On-Python.git
```

### Step 2: Navigate to Project Folder
```bash
cd Play-Cricket-On-Python
```

### Step 3: Run the Game
```bash
python cricket.py
```

> Make sure Python 3 is installed

---

## Project Structure

```
Play-Cricket-On-Python/
│
├── cricket.py   # Main game file
├── README.md    # Project documentation
```

---

## Functions Overview

| Function | Description |
|--------|-------------|
| `user_bat()` | User bats first |
| `computer_bat()` | Computer bats first |
| `user_chase()` | User chases target |
| `computer_chase()` | Computer chases target |
| `get_input()` | Validates user input |

---

## Sample Gameplay

```
🏏 Hand Cricket: You vs Computer
Enter overs: 2
Enter players per team: 3
Toss (heads/tails): heads
You won toss! Bat or bowl? bat
Over 1 Ball 1 – Your run: 4
Computer bowled: 2
Score: 4/0
```

---

## Future Improvements

- GUI version using **Tkinter / Pygame**
- Difficulty levels (Easy / Medium / Hard)
- Match statistics & scoreboard
- Multiplayer mode

---

## Author

- **Shivam Singh**
- Student | Python Enthusiast
- @shivam183-star
---

## Support

If you like this project, please star the repository and share it!

Happy Coding & Enjoy Cricket

