import turtle

class Solution:
  def __init__(self, input_filename):
    self.input_filename = input_filename
    self.input_lines    = None

    # Grid of form [x][y]
    self.grid  = [[False] * 1000 for _ in range(1000)]
    self.grid2 = [[0]     * 1000 for _ in range(1000)]

  def __str__(self):
    return f'Solution One: {self.solution_one()} \n'\
      f'Solution Two: {self.solution_two()}'

  def solution_one(self):
    for line in self.__input_lines():
      [*instruction, start, _, end] = line.split()
      start = list(map(lambda x: int(x), start.split(',')))
      end   = list(map(lambda x: int(x), end.split(',')))

      if instruction[0] == 'toggle':
        self.__toggle(self.grid, start, end)
      elif instruction[0] == 'turn':
        self.__turn(self.grid, instruction[1], start, end)

    # self.__print_grid()

    return self.__lit_light_count()

  def solution_two(self):
    for line in self.__input_lines():
      [*instruction, start, _, end] = line.split()
      start = list(map(lambda x: int(x), start.split(',')))
      end   = list(map(lambda x: int(x), end.split(',')))

      if instruction[0] == 'toggle':
        self.__modify(self.grid2, start, end, 2)
      elif instruction[0] == 'turn':
        if instruction[1] == 'on':
          self.__modify(self.grid2, start, end, 1)
        else:
          self.__modify(self.grid2, start, end, -1)

    return self.__total_brightness()

  def __toggle(self, grid, start, end):
    # print(f'Toggle {start} - {end}')
    for x in range(start[0], end[0] + 1):
      for y in range(start[1], end[1] + 1):
        grid[x][y] = not grid[x][y]

  def __turn(self, grid, value, start, end):
    # print(f'Turn {value} {start} - {end}')
    for x in range(start[0], end[0] + 1):
      for y in range(start[1], end[1] + 1):
        grid[x][y] = (value == 'on')

  def __modify(self, grid, start, end, value):
    # print(f'Turn {value} {start} - {end}')
    for x in range(start[0], end[0] + 1):
      for y in range(start[1], end[1] + 1):
        grid[x][y] += value

        if grid[x][y] < 0:
          grid[x][y] = 0

  def __lit_light_count(self):
    count = 0
    for column in self.grid:
      # print(f'{column} {column.count(True)}')
      count += column.count(True)

    return count

  def __total_brightness(self):
    count = 0
    for column in self.grid2:
      count += sum(column)

    return count


  def __print_grid(self):
    turtle.screensize(1000, 1000)
    turtle.color('black', 'black')
    turtle.speed(0)
    turtle.penup()
    turtle.tracer(10000)

    for x in range(0, 1000):
      for y in range(0, 1000):
        if self.grid[x][y]:
          print(f'Drawing {[x, y]}')
          turtle.goto(x - 500, y - 500)
          turtle.begin_fill()
          for _ in range(0, 4):
            turtle.forward(1)
            turtle.left(90)
          turtle.end_fill()

    turtle.done()

  def __input_lines(self):
    if self.input_lines == None:
      input_stream     = open(self.input_filename, 'r')
      self.input_lines = input_stream.readlines()

    return self.input_lines

print(Solution('input.txt'))
