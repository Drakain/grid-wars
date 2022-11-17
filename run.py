import random
import time


# GLOBAL VARIABLES #

# Variable for grid
grid = [[]]
# Variable for grid size
grid_size = 10
# Variable for number of ships
ships = 5
# Variable for ship positions
ship_positions = [[]]
# Variable for number of ships sunk
ships_sunk = 0
# Variable for bullets left
missiles = 30
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


def valid_coordinate():
    """
    Checks if the coordinates entered by the player are inside the grid.
    """

    global grid
    global alphabet

    is_valid_coordinate = False
    row = -1
    col = -1

    while is_valid_coordinate is False:
        coordinate = input('Enter a coordinate within the grid: ')
        coordinate = coordinate.upper()
        if len(coordinate) <= 0 or len(coordinate) > 2:
            print('Please enter only one valid row coordinate together with a valid column coordinate.')
            continue
        row = coordinate[0]
        col = coordinate[1]
        if not row.isalpha() or not col.isnumeric():
            print('Please enter a letter (A-J) for row and a number (0-9) for column.')
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print('Please enter a letter (A-J) for row and a number (0-9) for column.')
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print('Please enter a letter (A-J) for row and a number (0-9) for column.')
            continue
        if grid[row][col] == '#' or grid[row][col] == 'X':
            print('You have already attacked this position. Try another!')
            continue
        if grid[row][col] == '.' or grid[row][col] == 'O':
            is_valid_coordinate = True

    return row, col


def check_if_destroyed(row, col):
    """
    Checks if all parts of a ship have been hit and increments number destroyed ships.
    """

    global grid
    global ship_positions

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != 'X':
                        return False
    return True


def shoot_missile():
    """
    Updates the grid and ship status based on where a missile was shot.
    """

    global grid
    global ships_sunk
    global missiles

    row, col = valid_coordinate()
    print('')
    print('--------------------')

    if grid[row][col] == '.':
        print('You missed...')
        grid[row][col] = '#'
    elif grid[row][col] == 'O':
        print('A ship was hit!')
        grid[row][col] = 'X'
        if check_if_destroyed(row, col):
            print('A ship has been completely destroyed!')
            ships_sunk += 1
        else:
            print('A ship has been damaged.')

    missiles -= 1








def run():
    """
    Main function that runs the game.
    """

    global game_over

    generate_grid()
    show_grid()
    check_grid_and_place_ship()
    attempt_ship_placement()



run()