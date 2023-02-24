#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
    grid: a list of list of integers. 0 represents a water zone, 1 represents a land zone.
    One cell is a square with side length 1. Grid cells are connected horizontally/vertically (not diagonally).
    Grid is rectangular, width and height don’t exceed 100. Grid is completely surrounded by water, and there is one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island).

    Returns:
    perimeter: an integer representing the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Start with the assumption that this cell contributes 4 sides to the perimeter
                if row > 0 and grid[row-1][col] == 1:  # If there is a land cell to the north, subtract 1 from the perimeter
                    perimeter -= 1
                if row < rows - 1 and grid[row+1][col] == 1:  # If there is a land cell to the south, subtract 1 from the perimeter
                    perimeter -= 1
                if col > 0 and grid[row][col-1] == 1:  # If there is a land cell to the west, subtract 1 from the perimeter
                    perimeter -= 1
                if col < cols - 1 and grid[row][col+1] == 1:  # If there is a land cell to the east, subtract 1 from the perimeter
                    perimeter -= 1

    return perimeter
