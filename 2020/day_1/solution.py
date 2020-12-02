class DayOne:
  def __init__(self, input_file, target_value):
    self.input_file   = input_file
    self.target_value = target_value
    self.input_array  = None

  def print_solutions(self):
    print(f'Part One: {self.part_one()}')
    print(f'Part Two: {self.part_two()}')

  def part_one(self):
    input_array = self.fetch_input_array()

    for x in input_array:
      target_pair = self.target_value - x

      if target_pair in input_array:
        return x * target_pair

  def part_two(self):
    input_array = self.fetch_input_array()

    input_array.sort()

    for x in input_array:
      target_sum = self.target_value - x

      for y in input_array:
        if x + y > self.target_value:
          break

        target_pair = target_sum - y

        if target_pair in input_array:
          return x * y * target_pair;

  def fetch_input_array(self):
    if self.input_array != None:
      return self.input_array

    input_stream = open(self.input_file, 'r')
    input_lines = input_stream.readlines()
    input_lines = list(map(lambda num: int(num.rstrip()), input_lines))

    return input_lines

DayOne('input.txt', 2020).print_solutions()
