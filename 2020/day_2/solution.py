import re

def solution_one(input_lines):
  count = 0

  for password_input in input_lines:
    [min_max, letter, password] = password_input.split()
    [letter_min, letter_max]    = list(map(lambda num: int(num), min_max.split('-')))
    letter                      = letter[0]
    letter_count                = password.count(letter)

    if letter_count >= letter_min and letter_count <= letter_max:
      count += 1

  return count

def solution_two(input_lines):
  count = 0

  for password_input in input_lines:
    [position_indexes, letter, password] = password_input.split()
    position_indexes                     = list(map(lambda num: int(num) - 1, position_indexes.split('-')))
    letter                               = letter[0]

    if (password[position_indexes[0]] == letter) ^ (password[position_indexes[1]] == letter):
      count += 1

  return count

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()
input_lines = list(map(lambda num: num.rstrip(), input_lines))

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
