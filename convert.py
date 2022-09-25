# Configuration
INPUT_FILE_NAME = "input.txt"

input_file = open(INPUT_FILE_NAME, "r")
input_file_lines = input_file.readlines()

row_dict_arr = []

for row_str in input_file_lines:
  split_values = row_str.strip().split(",")
  print(split_values)