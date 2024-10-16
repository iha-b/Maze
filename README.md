# Maze Game

## Description

The Maze Game is a Python-based application that utilizes stacks to navigate through mazes. Players can input their own mazes represented as 2D lists, and the program will find a path to the goal ('G') using a stack-based approach. The maze-solving algorithm follows a counterclockwise traversal strategy, replacing visited spaces with step counts, allowing users to visualize the path taken.

## Features

- Stack-based maze-solving algorithm.
- Customizable maze input.
- Step count tracking and visualization.
- Pytest support for unit testing the solution.

## Usage

1. **Run the Maze Solver**: Execute the `lab04.py` file to start the maze solver.
2. **Input a Maze**: You can define your maze in the code using a 2D list format.
3. **Solve the Maze**: The program will display the maze with step counts marking the path taken to reach the goal.

## Instructions

For this project, you will need to create three files:

- `MazeTraversal.py`: Contains the implementation of the `solveMaze` function that navigates through the maze.
- `Stack.py`: Contains the definition of a Stack class using Python lists.
- `testFile.py`: Includes pytest functions to validate the functionality of your maze solver.

## How to Represent a Maze

A maze is represented as a 2D list. Each element can be one of the following:

- `' '` - An empty space (can be moved into).
- `'+'` - A wall (cannot be moved into).
- `'G'` - The goal (the target position).

### Example Maze Representation

```python
maze = [
    ['+','+','+','+','G','+'],
    ['+',' ','+',' ',' ','+'],
    ['+',' ',' ',' ','+','+'],
    ['+',' ','+','+',' ','+'],
    ['+',' ',' ',' ',' ','+'],
    ['+','+','+','+','+','+']
]
```
## Traversing the Maze

The algorithm will:

- Start at a given coordinate and check for valid moves in a counterclockwise order: North, West, South, East.
- Replace spaces with step counts as it progresses.
- Stop once it reaches the goal or exhausts all options.

## Example Maze

An example maze and its corresponding output after solving is shown below:

### Initial Maze:

```python
maze = [
    ['+', '+', '+', '+', 'G', '+'],
    ['+', ' ', '+', ' ', ' ', '+'],
    ['+', ' ', ' ', ' ', '+', '+'],
    ['+', ' ', '+', '+', ' ', '+'],
    ['+', ' ', ' ', ' ', ' ', '+'],
    ['+', '+', '+', '+', '+', '+']
]

### Maze After Solving:

```python
maze = [
    ['+', '+', '+', '+', 'G', '+'],
    ['+', 8, '+', 11, 12, '+'],
    ['+', 7, 9, 10, '+', '+'],
    ['+', 6, '+', '+', 2, '+'],
    ['+', 5, 4, 3, 1, '+'],
    ['+', '+', '+', '+', '+', '+']
]

## Contributions

Feel free to fork the repository, make changes, and create pull requests to contribute to the project!



