#!/usr/bin/python3
"""Island Perimeter."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid: List of list of integers representing the island.
    Returns:
        The perimeter of the island.
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4  # Add 4 for each land cell

                # Check adjacent cells
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract 2 if the cell above is land
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract 2 if the cell on the left

    return perimeter
