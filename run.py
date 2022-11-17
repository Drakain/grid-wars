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


def attempt_ship_placement(row, col, direction, length):
    """
    Attempts to place a ship on the grid based on direction with help from the above method.
    """

    global grid_size


def generate_grid():
    """
    Generates a 10x10 grid and attempts to randomly place down different types of ships at different locations
    """

    global grid
    global grid_size
    global ships
    global ship_positions


def show_grid():
    """
    Will show the grid with rows A-J and columns 0-9
    """

    global grid
    global alphabet