def solution_one(input_lines):
  x = 0
  y = 0
  width = len(input_lines[0])
  tree_count = 0

  for line in input_lines:
    if line[x % width] == '#':
      tree_count += 1

    y += 1
    x += 3

  return tree_count

def solution_two(input_lines):
  width = len(input_lines[0])
  tree_count = 1

  slopes = [
    { 'x': 1, 'y': 1 },
    { 'x': 3, 'y': 1 },
    { 'x': 5, 'y': 1 },
    { 'x': 7, 'y': 1 },
    { 'x': 1, 'y': 2 }
  ]

  for slope in slopes:
    current_y = 0
    x = 0
    y = 0

    slope_tree_count = 0
    for line in input_lines:
      if current_y != y:
        current_y += 1
        continue

      if line[x % width] == '#':
        slope_tree_count += 1

      y += slope['y']
      x += slope['x']

      current_y += 1
    
    print(slope_tree_count)
    tree_count *= slope_tree_count

  return tree_count

input_stream = open('./input.txt', 'r')
input_lines  = input_stream.readlines()
input_lines  = list(map(lambda line: line.rstrip(), input_lines))

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
