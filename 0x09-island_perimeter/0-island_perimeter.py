#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Each land cell starts with 4 potential sides
                perimeter += 4

                # Check the cell above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Shared edge with the cell above

                # Check the cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Shared edge with the cell to the left

    return perimeter
