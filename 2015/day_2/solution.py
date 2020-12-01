def solution_one(input_lines):
  running_sum = 0
  for input_line in input_lines:
    sides = input_line.split('x')
    sides = list(map(lambda num: int(num.rstrip()), sides))
    sides.sort()

    surface_area = \
      2 * sides[0] * sides[1] + \
      2 * sides[1] * sides[2] + \
      2 * sides[2] * sides[0]

    smallest_side = sides[0] * sides[1]

    running_sum += surface_area + smallest_side

  return running_sum

def solution_two(input_lines):
  running_sum = 0
  for input_line in input_lines:
    sides = input_line.split('x')
    sides = list(map(lambda num: int(num.rstrip()), sides))
    sides.sort()

    smallest_perimeter = 2 * (sides[0] + sides[1])
    volume             = sides[0] * sides[1] * sides[2]

    running_sum += smallest_perimeter + volume

  return running_sum

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')

