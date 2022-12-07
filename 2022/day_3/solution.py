def solution_one(input_lines):
  total_score = 0
  for line in input_lines:
    line = line.strip()

    half_length = int(len(line) / 2)
    first_half = line[0:half_length]
    second_half = line[half_length:]

    for character in first_half:
      if character in second_half:
        if character.isupper():
          total_score += ord(character) - 64 + 26
        else:
          total_score += ord(character) - 96

        break

  return total_score

def solution_two(input_lines):
  total_score = 0
  container = []
  for line in input_lines:
    line = line.strip()
    container.append(line)

    if len(container) % 3 != 0:
      continue

    for character in container[0]:
      if character in container[1] and character in container[2]:
        if character.isupper():
          total_score += ord(character) - 64 + 26
        else:
          total_score += ord(character) - 96

        break

    container = []

  return total_score

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
