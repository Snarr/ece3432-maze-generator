class MazeConverter:
  def __init__(self):
    print("New maze converter instantiated")
    
  def convert(self, input_file, output_file):
    # Open input file for file reading
    input_file = open(input_file, "r")

    # Get array of lines in file
    input_file_lines = input_file.readlines()

    row_dict_arr, max_x, max_y = self.read_lines_to_dict_arr(input_file_lines)

    maze_matrix = self.initialize_wall_matrix(max_x, max_y)

    maze_matrix = self.store_wall_matrix(row_dict_arr,maze_matrix)

    self.write_to_file(maze_matrix, output_file)
  
   
  # Define function for checking if there is a wall (0 == wall, 1 == no wall)
  def check_if_wall(self, distance):
    return (1 if (distance > 0.25) else 0)

  # Convert lines to array of dictionaries, each containing one-line worth of information
  # Also store max_x and max_y from the maze for determining its size
  def read_lines_to_dict_arr(self, lines):
    row_dict_arr = []
    max_x = 0
    max_y = 0
    # Read rows and store their data into dictionaries
    # Also store maximum X and Y values read to determine size of maze
    for row_str in lines:
      split_values = row_str.strip().split(",")
      row_dict = {}

      row_dict["x"] = int(split_values[0][2:])
      row_dict["y"] = int(split_values[1].split(')')[0].strip())

      row_dict["walls"] = [float(wall) for wall in split_values[2:]]
      
      if (row_dict["x"] > max_x): max_x = row_dict["x"]
      if (row_dict["y"] > max_y): max_y = row_dict["y"]

      row_dict_arr.append(row_dict)
    return (row_dict_arr, max_x, max_y)

  # Initialize a 3D matrix matching the size of the maze with 4 walls inside
  def initialize_wall_matrix(self, max_x, max_y):
    # Build 3D array
    # 1st: rows, size of max_y
    # 2nd: columns, size of max_x
    # 3rd: walls, size of 4, initialize to 1
    return [[[1 for w in range(4)] for x in range(max_x)] for y in range(max_y)]

  # Store walls from unordered array of dictionaries to maze matrix
  def store_wall_matrix(self, row_dict_arr, maze_matrix):
    # Store wall array to each coordinate in the [row, column] matrix
    for row_dict in row_dict_arr:
      x = row_dict["x"]-1 # Subtract 1 because Arrays are indexed starting at 0
      y = row_dict["y"]-1 # Subtract 1 because Arrays are indexed starting at 0

      # Make new array of wall states from distances (0 == wall, 1 == no wall)
      maze_matrix[y][x] = [self.check_if_wall(wall) for wall in row_dict["walls"]]
    return maze_matrix

  # Write the maze matrix to an output file
  def write_to_file(self, maze_matrix, output_file):
    # Open output file for file writing
    output_file = open(output_file, "w")

    # Write key to top of file
    output_file.write("  cell  ,E,W,N,S\n")

    # Loop through maze matrix and output formatted line containing coordinate information
    for i, row in enumerate(maze_matrix):
        for j, col in enumerate(row):
          output_file.write(f"\"({j+1}, {i+1})\",{col[0]},{col[2]},{col[3]},{col[1]}\n")
