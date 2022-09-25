# Configuration
INPUT_FILE_NAME = "input.txt"

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

print(f"{max_x}, {max_y}")