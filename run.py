import random
import time


# GLOBAL VARIABLES #

# Variable for grid
grid = [[]]
# Variable for grid size
grid_size = 10
# Variable for number of ships
ships = 0
# Variable for ship positions
ship_positions = [[]]
# Variable for number of ships sunk
ships_sunk = 0
# Variable for bullets left
bullets = 30
# Variable for game over
game_over = False
# Variable for alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'


def check_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Will check grid to see if it is possible to place a ship at the location.
    """

    global grid
    global ship_positions

    pos_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != '.':
                pos_valid = False
                break
    if pos_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = 'O'
    return pos_valid


def attempt_ship_placement(row, col, direction, length):
    """
    Attempts to place a ship on the grid based on direction with help from the above method.
    """

    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == 'left':
        if col - length < 0:
            return False
        start_col = col - length + 1
    elif direction == 'right':
        if col + length >= grid_size:
            return False
        end_col = col + length
    elif direction == 'up':
        if row - length < 0:
            return False
        start_row = row - length + 1
    elif direction == 'down':
        if row + length >= grid_size:
            return False
        end_row = row + length

    return check_grid_and_place_ship(start_row, end_row, start_col, end_col)

      
def generate_grid():
    """
    Generates a 10x10 grid and attempts to randomly place down different types of ships at different locations.
    """

    global grid
    global grid_size
    global ships
    global ship_positions

    random.seed(time.time())

    rows, cols = grid_size, grid_size

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append('.')
        grid.append(row)

    ships_placed = 0

    ship_positions = []

    while ships_placed != ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(['up', 'down', 'right', 'left'])
        ship_size = random.randint(3, 5)
        if attempt_ship_placement(random_row, random_col, direction, ship_size):
            ships_placed += 1


def show_grid():
    """
    Will show the grid with rows A-J and columns 0-9.
    """

    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=' ')
        for col in range(len(grid[row])):
            if grid[row][col] == 'O':
                if debug_mode:
                    print('O', end=' ')
                else: 
                    print('.', end=' ')
            else:
                print(grid[row][col], end=' ') 
        print('')

    print(' ', end=' ')
    for x in range(len(grid[0])):
        print(str(x), end=' ')
    print('')
