def solution_one(input_string):
  return input_string.count('(') - input_string.count(')')

def solution_two(input_string):
  current_floor = 0
  for char_index in range(0, len(input_string) - 1):
    char = input_string[char_index]

    if char == '(':
      current_floor += 1
    elif char == ')':
      current_floor -= 1

    if current_floor < 0:
      return char_index + 1

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()
input_string = input_lines[0]

print(f'Solution One: {solution_one(input_string)}')
print(f'Solution Two: {solution_two(input_string)}')

