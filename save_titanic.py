def create_ocean(size):
    """Create a square ocean grid of the given size."""
    return [['🟦'] * size for _ in range(size)]

def set_cell(ocean, x, y, value):
    """Set a specific cell in the ocean grid to the given value."""
    if 0 <= x < len(ocean) and 0 <= y < len(ocean[0]):
        ocean[x][y] = value

def draw_ocean(ocean):
    """Print the current state of the ocean grid."""
    for row in ocean:
        print(''.join(row))
    print()

def is_iceberg_nearby(ocean, row, col, size=3):
    """Check if there are any icebergs in a given range around the Titanic."""
    # Ensure the 'ocean' grid is passed, not individual elements
    for i in range(max(0, row - size), min(len(ocean), row + size + 1)):
        for j in range(max(0, col - size), min(len(ocean[0]), col + size + 1)):
            if ocean[i][j] == '🧊':
                return True
    return False

def auto_pilot_next_step(titanic_row, titanic_col, ocean):
    """Decide the next move for the Titanic based on the current position and nearby icebergs."""
    # Ensure the ocean grid is passed, and check surrounding cells for safety
    if titanic_col > 0 and not is_iceberg_nearby(ocean, titanic_row, titanic_col - 1):
        return 'WEST'  # Move west if it's safe
    if titanic_row > 0 and not is_iceberg_nearby(ocean, titanic_row - 1, titanic_col):
        return 'NORTH'  # Move north if it's safe
    if titanic_row < len(ocean) - 1 and not is_iceberg_nearby(ocean, titanic_row + 1, titanic_col):
        return 'SOUTH'  # Move south if it's safe
    if titanic_col < len(ocean[0]) - 1 and not is_iceberg_nearby(ocean, titanic_row, titanic_col + 1):
        return 'EAST'  # Move east if it's safe
    
    # If there's no safe direction, the Titanic stays put to avoid collision
    return 'WEST'

def move_titanic(ocean, titanic_pos, direction):
    """Move the Titanic in the given direction, updating the ocean grid."""
    new_row, new_col = titanic_pos
    if direction == 'NORTH':
        new_row -= 1
    elif direction == 'WEST':
        new_col -= 1
    elif direction == 'SOUTH':
        new_row += 1
    elif direction == 'EAST':
        new_col += 1

    # Check if the new position is valid (inside the ocean grid)
    if 0 <= new_row < len(ocean) and 0 <= new_col < len(ocean[0]):
        set_cell(ocean, new_row, new_col, "🚢")  # Place Titanic at new position
        set_cell(ocean, titanic_pos[0], titanic_pos[1], "🟦")  # Clear the previous position
        return new_row, new_col
    return titanic_pos  # Return the original position if the move is invalid

def simulate_titanic(ocean_size, titanic_pos, iceberg_pos):
    """Simulate the Titanic navigation avoiding icebergs, updating the ocean grid each turn."""
    ocean = create_ocean(ocean_size)
    set_cell(ocean, titanic_pos[0], titanic_pos[1], "🚢")  # Place Titanic
    set_cell(ocean, iceberg_pos[0], iceberg_pos[1], "🧊")  # Place iceberg

    # Simulate until the Titanic reaches the west side (column 0)
    while titanic_pos[1] > 0:
        direction = auto_pilot_next_step(titanic_pos[0], titanic_pos[1], ocean)  # Get next move
        titanic_pos = move_titanic(ocean, titanic_pos, direction)  # Move Titanic
        draw_ocean(ocean)  # Draw the ocean grid after each move

# Example Usage
ocean_size = 10
titanic_pos = [4, 7]  # Starting position of Titanic
iceberg_pos = [4, 2]  # Position of Iceberg

simulate_titanic(ocean_size, titanic_pos, iceberg_pos)
