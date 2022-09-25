# Configuration
INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

input_file = open(INPUT_FILE_NAME, "r")
input_file_lines = input_file.readlines()

row_dict_arr = []

max_x = 0
max_y = 0

for row_str in input_file_lines:
  split_values = row_str.strip().split(",")

  row_dict = {}

  row_dict["x"] = int(split_values[0][2:])
  row_dict["y"] = int(split_values[1].split(')')[0].strip())

  row_dict["walls"] = [float(wall) for wall in split_values[2:]]

  if (row_dict["x"] > max_x): max_x = row_dict["x"]
  if (row_dict["y"] > max_y): max_y = row_dict["y"]

  row_dict_arr.append(row_dict)

print(f"{max_x}, {max_y}")

maze_matrix = [[[1 for w in range(4)] for x in range(max_x)] for y in range(max_y)]

def check_if_wall(distance):
  return (1 if (distance > 0.25) else 0)

for row_dict in row_dict_arr:
   x = row_dict["x"]-1
   y = row_dict["y"]-1
   maze_matrix[y][x] = [check_if_wall(wall) for wall in row_dict["walls"]]

output_file = open(OUTPUT_FILE_NAME, "w")

for i, row in enumerate(maze_matrix):
    for j, col in enumerate(row):
      output_file.write(f"\"({j}, {i})\",{col[0]},{col[2]},{col[3]},{col[1]}\n")