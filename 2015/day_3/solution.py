def solution_one(input_string):
  # First hash is x, second is y
  visited_locations = []

  current_location = { 'x': 0, 'y': 0 }
  for direction in input_string:
    if direction == '<':
      current_location['x'] -= 1
    elif direction == '>':
      current_location['x'] += 1
    elif direction == '^':
      current_location['y'] += 1
    elif direction == 'v':
      current_location['y'] -= 1

    location_string = "%s-%s" % (current_location['x'], current_location['y'])
    if location_string not in visited_locations:
      visited_locations.append(location_string)

  return len(visited_locations)

def solution_two(input_string):
  # First hash is x, second is y
  visited_locations = []
  for santa_directions in [input_string[::2], input_string[1::2]]:
    current_location = { 'x': 0, 'y': 0 }
    for direction in santa_directions:
      if direction == '<':
        current_location['x'] -= 1
      elif direction == '>':
        current_location['x'] += 1
      elif direction == '^':
        current_location['y'] += 1
      elif direction == 'v':
        current_location['y'] -= 1

      location_string = "%s-%s" % (current_location['x'], current_location['y'])
      if location_string not in visited_locations:
        visited_locations.append(location_string)

  return len(visited_locations)

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()
input_string = input_lines[0]

print(f'Solution One: {solution_one(input_string)}')
print(f'Solution Two: {solution_two(input_string)}')

