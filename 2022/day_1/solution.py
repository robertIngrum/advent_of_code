def solution_one(input_lines):
  max_calories = 0
  current_calories = 0
  for line in input_lines:
    if line.strip() == "":
      current_calories = 0
      continue

    current_calories += int(line.strip())
    max_calories = max(max_calories, current_calories)

  return max_calories

def solution_two(input_lines):
  max_calories = []
  current_calories = 0
  for line in input_lines:
    if line.strip() == "":
      max_calories.append(current_calories)
      max_calories.sort(reverse=True)
      del max_calories[3:]
      current_calories = 0
      continue

    current_calories += int(line.strip())

  return sum(max_calories)

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
