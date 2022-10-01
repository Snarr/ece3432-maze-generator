# ECE-3432 Maze Generator

This program was developed for an assignment in my ECE 3432 "Robotic Control using Raspberry Pi Microcontroller" elective course. The goal of this program is to take in an unordered list of data about wall locations within a maze and outputs an ordered list of said data, optimized for use with the Pyamaze library. My implementation works for mazes of any size by storing the maximum X and Y coordinate values when initially reading the unordered wall location data points. 

The output of this program is designed to be used with the Pyamaze package for generating mazes with Python. [Check out Pyamaze here](https://github.com/MAN1986/pyamaze).

# Usage

1. Place the `MazeConverter.py` file in the same directory as your program. Alternatively, install the `MazeConverter.py` file to your Python packages.

2. Use the following code to get started:

```
# Import package
from MazeConverter import MazeConverter

# Make new instance of a Maze Converter
mazeConverter = MazeConverter()

# Use the convert command with an Input File Path (string) and an Output File Path (string)
mazeConverter.convert("./input.txt", "./output.txt")

```

## Input

The program reads through input files assuming the following format on each line:

```
"(3, 2)",0.22,1.2,0.14,1.8
... <more lines below>
```

- Where the X coordinate of the point is 3, the Y coordinate of the point is 2, the distance to the Eastern-most wall is 0.22 meters, the distance to the Southern-most wall is 1.2 meters, the distance to the Western-most wall is 0.14 meters, and the distance to the Northern-most wall is 1.8 meters.

## Output

The program outputs wall location data in the following format:

```
  cell  ,E,W,N,S
"(3, 2)",0,0,1,1
... <more lines below>
```
- Where the X coordinate of the point is 3, the Y coordinate of the point is 2, with each "0" indicating a wall in that direction (denoted if distance is <= 0.25 meters) and each "1" indicating no wall before the next coordinate point (denoted if distance is > 0.25 meters).

# Notes
- Program decides if walls are present if they are within `0.25 meters` of distance in a given direction.
- "0" in the output indicates a wall (according to pyamaze)
- "1" in the output indicates no wall (according to pyamaze)
- The input file orders the wall directions "East, South, West, North" (assignment requirement)
- The output file orders the wall directions "East, West, North, South" (assignment requirement)
- If a point is missing, the program will assume that there are no walls immediately surrounding the point. (all 1's)