from lib2to3.pytree import convert
from MazeConverter import MazeConverter

converter = MazeConverter()

converter.convert("./input.txt", "./output.txt")