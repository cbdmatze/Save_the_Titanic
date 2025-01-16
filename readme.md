---

🚢 Save the Titanic: Enhanced Edition 🧊

Save the Titanic is a fun and engaging Python simulation where the Titanic must navigate through a treacherous ocean filled with dangerous icebergs. The goal is to guide the Titanic safely across the ocean to the western edge, avoiding collisions with icebergs. Now featuring multiple icebergs, random ocean generation, and both AI autopilot and interactive user-controlled mode!



📝 Description

In this enhanced version of Save the Titanic, the Titanic (🚢) navigates a grid-based ocean (🟦) filled with deadly icebergs (🧊). The challenge? Guide the Titanic safely to the western edge of the ocean while avoiding collisions with multiple icebergs scattered randomly across the grid.



The simulation offers two modes:


AI Autopilot Mode: 

The Titanic uses the A* pathfinding algorithm to navigate the shortest and safest route to the western edge.


Interactive Mode: 

You take control of the Titanic, deciding its movements manually in real-time!



🚀 Features


🌊 Dynamic Ocean Grid with Multiple Icebergs

The simulation generates a square ocean grid of customizable size with a specified number of icebergs placed randomly.
The Titanic starts in the eastern part of the grid and must move west to reach safety.



🤖 AI Autopilot with A* Pathfinding

The AI autopilot uses the A* search algorithm to compute the optimal and safest path for the Titanic to reach the western edge.
The algorithm considers nearby icebergs and intelligently navigates to avoid collisions while minimizing travel time.



🎮 Interactive Mode

In Interactive Mode, you control the Titanic's movements, deciding whether to move NORTH, SOUTH, EAST, or WEST on each turn.
The ocean grid updates after every move, visually displaying the Titanic's new position and any nearby icebergs.



🛠️ Customizable Settings


Ocean Size: 

Adjust the size of the ocean grid to increase or decrease the difficulty.
Iceberg Count: 

Specify the number of icebergs to be randomly placed in the ocean, adding to the challenge.



🔧 How It Works


Simulation Steps:


Ocean Grid Generation: 

The ocean is generated as a square grid of the specified size, filled with water (🟦). Random icebergs (🧊) are placed in the grid.



Titanic Movement:


In AI Mode: 

The Titanic automatically navigates using the A* pathfinding algorithm, avoiding icebergs and heading west.


In Interactive Mode: 

The user manually controls the Titanic's movements.


Pathfinding with A*: 

The Titanic uses the A* algorithm to compute the shortest and safest path to the western edge of the ocean, taking into account nearby icebergs and prioritizing safety.


Victory Condition: 

The simulation runs until the Titanic successfully reaches the western edge (column 0) or gets stuck due to surrounding icebergs.



📚 Code Structure



create_ocean(size, iceberg_count): 

Generates an ocean grid of the given size with the specified number of randomly placed icebergs.



set_cell(ocean, x, y, value): 

Updates a specific cell in the ocean grid with a given value (Titanic or iceberg).


draw_ocean(ocean): 

Prints the current state of the ocean grid.


is_iceberg_nearby(ocean, row, col, size=3): 

Checks if there are any icebergs within a given range around the Titanic.


get_neighbors(pos, ocean): 

Returns valid neighboring cells for a given position, considering ocean boundaries and avoiding icebergs.


a_star_search(start, goal, ocean): 

The A* search algorithm to compute the optimal path from the Titanic's starting position to the western edge, avoiding icebergs.


move_titanic(ocean, titanic_pos, direction): 

Moves the Titanic in the specified direction and updates the ocean grid.


simulate_titanic(ocean_size, titanic_pos, iceberg_count, interactive=False): 

Runs the simulation in either AI Mode (default) or Interactive Mode based on user input.




🖥️ How to Run the Program


Clone the repository or download the script.

Open the Python script in your favorite IDE or editor.

Customize the ocean size, number of icebergs, Titanic’s starting position, and interactive mode as desired:


ocean_size = 10  # Set the size of the ocean grid
titanic_pos = [4, 7]  # Starting position of Titanic
iceberg_count = 10  # Number of icebergs in the ocean



Run the program:

bash

python save_the_titanic.py


Watch the Titanic's journey unfold in the console, with the ocean grid updating after each move. In interactive mode, enter your moves manually (e.g., NORTH, SOUTH, EAST, or WEST).




🎮 Modes


AI Autopilot Mode (Default):

The Titanic automatically navigates using A* pathfinding.



To run the simulation in AI mode, call:

python

simulate_titanic(ocean_size, titanic_pos, iceberg_count, interactive=False)



Interactive Mode:

In this mode, you control the Titanic's movements. After each move, the ocean grid updates to show the Titanic’s new position.


To enable interactive mode, call:

python

simulate_titanic(ocean_size, titanic_pos, iceberg_count, interactive=True)



🎮 Example Output
Here’s what the ocean grid might look like as the Titanic navigates through the icebergs:


🟦🟦🟦🟦🟦🧊🟦🟦🟦🟦
🟦🟦🧊🟦🟦🟦🟦🧊🟦🟦
🟦🟦🟦🧊🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🧊🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🚢🟦🟦
🟦🟦🧊🟦🟦🧊🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🧊🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🧊🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦


After each move, you’ll see the Titanic (🚢) move across the grid, avoiding icebergs (🧊), as it attempts to reach the safety of the western edge.




🌟 Customization


Ocean Size: 

Change the size of the ocean grid by modifying the ocean_size parameter.


Iceberg Count: 

Increase or decrease the number of icebergs by adjusting the iceberg_count parameter.


Interactive vs AI Mode: 

Enable or disable interactive mode by setting the interactive flag to True or False.



🛠️ Future Improvements


Dynamic Iceberg Movement: 

Add moving icebergs to increase the challenge.


Multiple Ships: 

Simulate multiple ships trying to navigate the ocean simultaneously.


Difficulty Levels: 

Create different difficulty settings based on iceberg density and ocean size.


Obstacle Variations: 

Add different types of obstacles, such as whirlpools or rocks, that the Titanic must avoid.



💡 Inspiration

This enhanced version of Save the Titanic was inspired by the challenge of safely navigating the Titanic through icy waters. It's a fun simulation for imagining alternative outcomes while testing out pathfinding algorithms and user interaction.



🔗 Contributing

If you'd like to contribute to this project or suggest enhancements, feel free to open a pull request or submit an issue.



📄 License

This project is licensed under the MIT License - see the LICENSE file for details.


Navigate the Titanic and steer clear of those icebergs! ❄️🧊🚢
---