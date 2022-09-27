from lib2to3.pytree import convert
from MazeConverter import MazeConverter

converter = MazeConverter()

converter.convert("./example/input.txt", "./example/output.txt")