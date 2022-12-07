def solution_one(input_lines):
  total_score = 0
  for line in input_lines:
    line = line.strip()

    splits = line.split(',')
    first_pair = list(map(int, splits[0].split('-')))
    second_pair = list(map(int, splits[1].split('-')))

    if first_pair[0] >= second_pair[0] and first_pair[1] <= second_pair[1]:
      total_score += 1
      continue

    if second_pair[0] >= first_pair[0] and second_pair[1] <= first_pair[1]:
      total_score += 1
      continue

  return total_score

def solution_two(input_lines):
  total_score = 0
  for line in input_lines:
    line = line.strip()

    splits = line.split(',')
    first_pair = list(map(int, splits[0].split('-')))
    second_pair = list(map(int, splits[1].split('-')))

    # 1 2 3 -
    # - 2 - -
    if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[0]:
      total_score += 1
      continue

    # - 2 - -
    # 1 2 3 -
    if second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[0]:
      total_score += 1
      continue

  return total_score

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
