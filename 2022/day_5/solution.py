STARTING_ARRAY = [
  ["R", "W", "F", "H", "T" , "S"],
  ["W", "Q", "D", "G", "S"],
  ["W", "T", "B"],
  ["J", "Z", "Q", "N", "T", "W", "R", "D"],
  ["Z", "T", "V", "L", "G", "H", "B", "F"],
  ["G", "S", "B", "V", "C", "T", "P", "L"],
  ["P", "G", "W", "T", "R", "B", "Z"],
  ["R", "J", "C", "T", "M", "G", "N"],
  ["W", "B", "G", "L"]
]

def copy_starting_array():
  stacks = []
  for line in STARTING_ARRAY:
    items = []
    for letter in line:
      items.append(letter)

    stacks.append(items)

  return stacks

def solution_one(input_lines):
  stacks = copy_starting_array()

  for line in input_lines:
    line = line.strip()
    line = line.replace("move ", "")
    line = line.replace("from ", "")
    line = line.replace("to ", "")

    count, start_stack, end_stack = list(map(int, line.split(" ")))

    start_stack -= 1
    end_stack -= 1

    items = stacks[start_stack][:count]
    items.reverse()
    stacks[start_stack] = stacks[start_stack][count:]
    stacks[end_stack] = items + stacks[end_stack]

  return "".join(list(map(lambda x: x[0], stacks)))

def solution_two(input_lines):
  stacks = copy_starting_array()

  for line in input_lines:
    line = line.strip()
    line = line.replace("move ", "")
    line = line.replace("from ", "")
    line = line.replace("to ", "")

    count, start_stack, end_stack = list(map(int, line.split(" ")))

    start_stack -= 1
    end_stack -= 1

    items = stacks[start_stack][:count]
    stacks[start_stack] = stacks[start_stack][count:]
    stacks[end_stack] = items + stacks[end_stack]

  return "".join(list(map(lambda x: x[0], stacks)))

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
