board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'W', 'B', '.', '.', '.'],
         ['.', '.', '.', 'B', 'W', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = ['1', '2', '3', '4', '5', '6', '7', '8']

B = 'B'
W = 'W'

players = {0: B, 1: W}

up = 'up',
up_right = 'up_right',
right = 'right',
down_right = 'down_right',
down = 'down',
down_left = 'down_left'
left = 'left',
up_left = 'up_left'

directions = {
    # follow clockwise
    1: up,
    2: up_right,
    3: right,
    4: down_right,
    5: down,
    6: down_left,
    7: left,
    8: up_left
}


def show_board(board):
    '''
    @functional: Print the board into the screen
    @input: matrix 2D (8 rows X 8 columns)
    @output: Do not return anything but print the board into the screen.
    @description:
        First line: Columns a -> h
        The next eight-line: Lines 1 -> 8
    '''
    print(end='  ')
    print(' '.join(cols))
    for x in range(len(rows)):
        print(rows[x], end=' ')
        for y in range(len(cols)):
            print(board[x][y], end=' ')
        print(end='\n')


def parse_player_step(str_choice):
    '''
    @functional: Convert player's step from string to int(row, col)
    @input: string - input of player's step
    @output: return (int, int) - (row, col) of the board
    @description:
        "d2" => row = 2; col = d
             => (row, col) = (1, 3) index from 0
    '''
    return (rows.index(str_choice[1]), cols.index(str_choice[0]))


def convert_to_string(x, y):
    '''
    @functional: Convert valid choices from int(x, y) to string.
    @input: (int, int) - (row, col) of the board
    @output: return string - the step.
    @description:
        (1,3) => "d2"
    '''
    return cols[y] + rows[x]


def is_boundary(x, y):
    if x == 0:
        return True
    if x == 7:
        return True
    if y == 0:
        return True
    if y == 7:
        return True
    return False


def move(row, col, direction):
    '''
    @functional: Define the next move from the current position
    @input:
        current position (int, int) - (row, col)
        given direction
    @output: return  (int, int) - (row, col)
             the next position of the given direction
    @description/logical:
        up: ignore the first line
        up_right: ignore the first line and the farest right line
        right: ignore the farest right line
        down_right: ignore the last line and the farest right line
        down: ignore the last line
        down_left: ignore the last line and the farest left line
        left: ignore the farest left line
        up_left: ignore the first line and the farest left line
    '''

    if direction == up and row > 0:
        return (row-1, col)
    elif direction == up_right and row > 0 and col < 7:
        return (row-1, col+1)
    elif direction == right and col < 7:
        return (row, col+1)
    elif direction == down_right and col < 7 and row < 7:
        return (row+1, col+1)
    elif direction == down and row < 7:
        return (row+1, col)
    elif direction == down_left and col > 0 and row < 7:
        return (row+1, col-1)
    elif direction == left and col > 0:
        return (row, col-1)
    elif direction == up_left and row > 0 and col > 0:
        return (row-1, col-1)
    return (row, col)


def get_enemies_line(board, x, y, player, direction):
    '''
    @functional: Find all enemies of the given direction
    @input:
        board (matrix 2D)
        coordinates(x, y)-(int, int)
        player's name: "W" or "B"
        given direction
    @output: return list enemies of the given direction
    @description/logical:
        Define the player and the enemies.
        Mark the cells follow the given direction.
        Keep moving until meet the player again.
    '''
    enemy = 'B' if player == 'W' else 'W'

    new_x, new_y = move(x, y, direction)
    enemy_line = []

    while board[x][y] == player and board[new_x][new_y] == enemy:
        enemy_line.append((new_x, new_y))
        new_x, new_y = move(new_x, new_y, direction)
        if is_boundary(new_x, new_y) is True:
            return enemy_line
    return enemy_line


def get_valid_choices(board, x, y, player, directions):
    '''
    @functional: Find all valid choices
    @input:
        board (matrix 2D)
        coordinates(x, y)-(int, int)
        player's name: "W" or "B"
        given direction
    @output: dictionary key=choice, value=enemies
    @description/logical:
        check 8 directions of each cell
            ...to get the valid choices and the enemies belong to them

    '''
    dict_eat = {}

    for direction in directions:
        enemy_line = get_enemies_line(board, x, y,
                                      player, directions[direction])
        if enemy_line != []:
            potential_position = move(enemy_line[-1][0],
                                      enemy_line[-1][1],
                                      directions[direction])
            if board[potential_position[0]][potential_position[1]] != player:
                dict_eat[convert_to_string(potential_position[0],
                         potential_position[1])] = enemy_line
    print(dict_eat)
    return dict_eat


def suggestion(board, player, directions):
    '''
    @functional:
    @input:
    @output:
    @description/logical:
    '''
    choices_enemies = []
    for x in range(len(rows)):
        for y in range(len(cols)):
            if board[x][y] == player:
                choices = get_valid_choices(board, x, y, player, directions)
                choices_enemies.append(choices)

    from collections import defaultdict
    merge_all = defaultdict(list)
    for d in choices_enemies:
        for key, value in d.items():
            merge_all[key].append(value)
    # print(merge_all)
    return merge_all


def eat(board, choices_enemies, user_choice, player):
    '''
    @functional:
    @input:
    @output:
    @description/logical:
    '''
    import itertools
    index_enemies = choices_enemies[user_choice]

    combined_enemies = itertools.chain.from_iterable(index_enemies)

    for position in combined_enemies:
        board[position[0]][position[1]] = player

    index_choice = parse_player_step(user_choice)
    board[index_choice[0]][index_choice[1]] = player

    return board


def is_end_game(board):
    '''
    @functional: Check to stop the game
    @input: board  matrix 2D
    @output: return True/ False
    @description/logical:
        If the board don't be filled, continue (False)
        else stop game (True)
    '''
    for sub_line in board:
        if '.' in sub_line:
            return False
    return True


def calculateScores(board):
    '''
    @functional: calculate the Score of player
    @input: board  matrix 2D
    @output: (int, int) score of player ("B"; "W")
    @description/logical:

    '''
    scoreW = 0
    scoreB = 0
    for x in range(len(rows)):
        for y in range(len(cols)):
            if board[x][y] == 'W':
                scoreW += 1
            if board[x][y] == 'B':
                scoreB += 1
    return (scoreB, scoreW)


def show_suggestion(choices_enemies, board):
    '''
    @functional: Mark the suggestions by the asterisk *
    @input: board - matrix 2D, list enemies
    @output: return the marked board by *
    @description/logical:
        Delete all asterisks of the previous suggestions
        Mark all the suggestions
    '''
    suggestion = list(choices_enemies.keys())

    for x in range(len(rows)):
        for y in range(len(cols)):
            if board[x][y] == '*':
                board[x][y] = '.'

    for pos in suggestion:
        x, y = parse_player_step(pos)
        board[x][y] = '*'

    return board


def end_game(board):
    print("End game")
    print('Score B - W: ', calculateScores(board))


if __name__ == "__main__":
    i = 0
    choice = ''
    while is_end_game(board) is False:

        current = i % 2
        choices_enemies = suggestion(board, players[current], directions)
        board = show_suggestion(choices_enemies, board)
        show_board(board)

        print('Step: ', i)
        print('Valid choices: ', end='')
        print(' '.join(choices_enemies.keys()))

        valid_choices = list(choices_enemies.keys())
        while choice not in valid_choices:
            choice = input('Player ' + players[current] + ': ')

        if len(valid_choices) == 0:
            is_end_game(board) is True

        board = eat(board, choices_enemies, choice, players[current])
        i += 1

    choices_enemies = suggestion(board, players[current], directions)
    show_board(board)
    end_game(board)
