﻿# GAME REVERSI - python3

Reversi is a strategy board game for two players, played on an 8×8 uncheckered board.

You can search more about the rules on the internet, even you can try a little at game online website.

[Play REVERSI Now](https://cardgames.io/reversi/).

### Enjoy the game

#### Clone my repository
```bash
git clone https://github.com/dinhnhu1401/REVERSI-GAME.git
cd REVERSI-GAME
python3 reversi.py

WELLCOME TO REVERSI GAME - BY MANDY DINH
Press 1: Play with machine (You are player B, machine is player W)
press 2: Two players
Press: _ 

(start game)

```

# Mission
Write a **light** version game of Reversi.

#### The game starts like this:
![start](src/1.png)

### First move:
The black player starts and gives a position among the valid choices. As you can see, the valid choices are given in alphabetical order.

![first_move](src/2.png)

### When a player cannot play
When a player cannot play, the game informs them.

![end](src/3.png)


### End condition
The game ends when both players cannot play anymore.

![result](src/4.png)

### Error handling
If the player plays something invalid, here is how you will handle it.
Putting it together.

Now, you also need to handle the case when a player doesn't have any valid move, as well as when both players don't have any move available.

Finally, when the game ends, you need to count the points.

# Analysis: Data structures and Functions

### Programming is basically functions and data structures.

- Use **list** in **list** to store a board.
First, we need a function to display the board. It's going turn a matrix like this:
```
[['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', 'W', 'B', '.', '.', '.'],
['.', '.', '.', 'B', 'W', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.']]
```
Into this:
```
  a b c d e f g h
1 . . . . . . . .
2 . . . . . . . .
3 . . . . . . . .
4 . . . W B . . .
5 . . . B W . . .
6 . . . . . . . .
7 . . . . . . . .
8 . . . . . . . .
```
- Then, we need a function to give us valid choices (*), depending on the player.
```
  a b c d e f g h
1 . . . . . . . .
2 . . . . . . . .
3 . . . * . . . .
4 . . * W B . . .
5 . . . B W * . .
6 . . . . * . . .
7 . . . . . . . .
8 . . . . . . . .
Step: 0
Valid choices: e6 c4 d3 f5
Player B:
```

- Finally, validate the player's choice and then replace all enemies between by wildcard character for the current player.
  Automatically check the valid choices for next player.
```
Player B: e6
  a b c d e f g h
1 . . . . . . . .
2 . . . . . . . .
3 . . . . . . . .
4 . . . W B * . .
5 . . . B B . . .
6 . . . * B * . .
7 . . . . . . . .
8 . . . . . . . .
Step: 1
Valid choices: e6 c4 d3 f5
Player W:
```
 
# Solution and related modules:

## Solution:

While the list of valid choice exits:

- Define the current player and then identify the enemy
- Go through the board, for each cell:
	- If the current cell is player:
		- Check 8 directions with this cell is the central cell, for each direction:
			- If the enemy is adjacent to the central cell and don't be surrounded by our troops, add to the list of valid choices and also record the position of all the enemies inside.
- Optimize player's choice by maximizing the number of enemies captured and display the list of valid choices by this order.
- When the current player **chooses** the next step, retrieve all enemies depends on the player's choice.

## Ralated mdules:

- Use **collections** import *defaultdict*
- Use **itertools**
  
# Coding Journey

|No               |Describe                              |Cause or Result       |
|-----------------|--------------------------------------|----------------------|
|1                | A stupid mess!                       | Distracted, not calm |
|2                | Omit the old and rebuild the new one | Ver 0.1 - 2 bugs     |
|3                | Write README Ver 0.1                 | The skeleton structure |
|4                | Bug 1: Can not find all the valid choices | Check wrong conditions, omit the asterisk case |
|5                | Bug 2: The loop of the game is broken| Forget to check the boundary - Ver 1.0.0 |
|6                | Write README Ver 0.2.                | Solution + Coding Journey |
|7                | Add comment and re-design code       | Ver 1.0.1 |
|8                | Bug 3: The loop of the game is overflow| Assign input of user - Ver 1.1.0 |
|9                |Edit pycodestyle + rename vars + Line alignment + re-structure init game| Light version 1.2.0
|10               | Add option 2 players or play with machine! | 1.3.0

@INTEKPROJECT