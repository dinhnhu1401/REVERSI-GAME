# Reversi - GAME - Python3
Reversi is a strategy board game for two players, played on an 8×8 uncheckered board.

You can search more about the rules on the internet, even you can try a little at [game online website ](https://cardgames.io/reversi/).



# Mission
You will write a **light** version game of Reversi.


#### The game starts like this:

![start](src/1.png)


## First move:

The black player starts and gives a position among the valid choices. As you can see, the valid choices are given in alphabetical order.

![first_move](src/2.png)

## When a player cannot play
When a player cannot play, the game informs them.

![end](src/3.png)

## End condition
The game ends when both players cannot play anymore.

![result](src/4.png)



# Analysis: functions
Programming is basically functions and data structures. 
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

Then, we need a function to give us valid choices, depending on the player.


# Error handling
If the player plays something invalid, here is how you will handle it.

Putting it together
Now, you also need to handle the case when a player doesn't have any valid move, as well as when both players don't have any move available.

Finally, when the game ends, you need to count the points.

Good luck!
