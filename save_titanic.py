import random
import heapq

# Constants
WATER = "🟦"
TITANIC = "🚢"
ICEBERG = "🧊"

def create_ocean(size, iceberg_count):
    """Create a square ocean grid of the given size and randomly place icebergs."""
    ocean = [[WATER] * size for _ in range(size)]
    
    # Place multiple icebergs randomly
    for _ in range(iceberg_count):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if ocean[x][y] == WATER:  # Place iceberg only on an empty cell
                ocean[x][y] = ICEBERG
                break
    return ocean

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
    for i in range(max(0, row - size), min(len(ocean), row + size + 1)):
        for j in range(max(0, col - size), min(len(ocean[0]), col + size + 1)):
            if ocean[i][j] == ICEBERG:
                return True
    return False

def get_neighbors(pos, ocean):
    """Get the valid neighboring cells for a given position."""
    row, col = pos
    neighbors = []
    moves = [('NORTH', (-1, 0)), ('SOUTH', (1, 0)), ('EAST', (0, 1)), ('WEST', (0, -1))]
    
    for direction, (d_row, d_col) in moves:
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < len(ocean) and 0 <= new_col < len(ocean[0]):
            if ocean[new_row][new_col] == WATER:  # Only return valid, non-iceberg cells
                neighbors.append(((new_row, new_col), direction))
    return neighbors

# Pathfinding using A* algorithm
def a_star_search(start, goal, ocean):
    """A* search to find the shortest path from start to goal."""
    def heuristic(pos):
        # Use Manhattan distance to estimate distance to the goal (west edge)
        return pos[1]
    
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current[1] == goal[1]:  # Reached the west side
            break
        
        for next_pos, direction in get_neighbors(current, ocean):
            new_cost = cost_so_far[current] + 1
            if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                cost_so_far[next_pos] = new_cost
                priority = new_cost + heuristic(next_pos)
                heapq.heappush(frontier, (priority, next_pos))
                came_from[next_pos] = (current, direction)
    
    # Reconstruct path
    path = []
    current = (goal[0], 0)
    while current and current in came_from:
        prev, direction = came_from[current]
        path.append(direction)
        current = prev
    return path[::-1] if path else []  # Return the reversed path

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
        set_cell(ocean, new_row, new_col, TITANIC)  # Place Titanic at new position
        set_cell(ocean, titanic_pos[0], titanic_pos[1], WATER)  # Clear the previous position
        return new_row, new_col
    return titanic_pos  # Return the original position if the move is invalid

def simulate_titanic(ocean_size, titanic_pos, iceberg_count, interactive=False):
    """Simulate the Titanic navigation using AI pathfinding or interactive mode."""
    ocean = create_ocean(ocean_size, iceberg_count)
    set_cell(ocean, titanic_pos[0], titanic_pos[1], TITANIC)  # Place Titanic

    # Get a goal at the western edge of the ocean
    goal = (titanic_pos[0], 0)

    if interactive:
        print("Starting interactive mode! Use 'NORTH', 'SOUTH', 'EAST', 'WEST' to move.")
    
    while titanic_pos[1] > 0:
        if interactive:
            draw_ocean(ocean)
            direction = input("Enter direction (NORTH, SOUTH, EAST, WEST): ").upper()
        else:
            # Use AI pathfinding to determine the next move
            path = a_star_search(titanic_pos, goal, ocean)
            if not path:
                print("The Titanic is stuck!")
                break
            direction = path[0]

        # Move Titanic and update the grid
        titanic_pos = move_titanic(ocean, titanic_pos, direction)
        draw_ocean(ocean)
    
    print("The Titanic has reached the western edge safely!" if titanic_pos[1] == 0 else "Game Over!")

# Example Usage
ocean_size = 10
titanic_pos = [4, 7]  # Starting position of Titanic
iceberg_count = 10  # Number of icebergs in the ocean

simulate_titanic(ocean_size, titanic_pos, iceberg_count, interactive=False)  # AI mode
# For interactive mode, set `interactive=True`
