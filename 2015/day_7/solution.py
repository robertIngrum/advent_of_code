def solution_one(input_lines):
  storage = {}

  for line in input_lines:
    [*instructions, _, target] = line.split()

    storage[target] = instructions

  keys_to_remove = []
  known_values = {}
  while known_values.get('a') == None:
    for key, instruction in storage.items():
      if len(instruction) == 1:
        if represents_int(instruction[0]):
          known_values[key] = int(instruction[0])
          keys_to_remove.append(key)
          continue
        elif known_values.get(instruction[0]) != None:
          known_values[key] = known_values.get(instruction[0])
          keys_to_remove.append(key)
          continue

      if len(instruction) == 2:
        # Must be NOT instruction
        if instruction[0] != 'NOT':
          print(f'Error on: {instruction}')
          continue

        if represents_int(instruction[1]):
          known_values[key] = (~ int(instruction[1])) + 2**16
          keys_to_remove.append(key)
          continue
        elif known_values.get(instruction[1]) != None:
          known_values[key] = (~ known_values.get(instruction[1])) + 2**16
          keys_to_remove.append(key)
          continue

      if (represents_int(instruction[0]) or known_values.get(instruction[0])) != None \
        and (represents_int(instruction[2]) or known_values.get(instruction[2])) != None:
        a = int(instruction[0]) if represents_int(instruction[0]) else known_values.get(instruction[0])
        b = int(instruction[2]) if represents_int(instruction[2]) else known_values.get(instruction[2])
        
        if instruction[1] == 'AND':
          known_values[key] = a & b
          keys_to_remove.append(key)
          continue
        elif instruction[1] == 'OR':
          known_values[key] = a | b
          keys_to_remove.append(key)
          continue
        elif instruction[1] == 'LSHIFT':
          known_values[key] = a << b
          keys_to_remove.append(key)
          continue
        elif instruction[1] == 'RSHIFT':
          known_values[key] = a >> b
          keys_to_remove.append(key)
          continue
        else:
          print(f'Error on: {instruction}')

    if len(keys_to_remove) == 0:
      # Either unsolvable or there's a bug, we need to debug.
      import pdb; pdb.set_trace()

    for key in keys_to_remove:
      storage.pop(key)
    keys_to_remove = []

  return known_values.get('a')

def solution_two(input_lines, solution_one):
  storage = {}

  for line in input_lines:
    [*instructions, _, target] = line.split()

    storage[target] = instructions

  # Modify b with the value from solution_one
  storage['b'] = [str(solution_one)]

  keys_to_remove = []
  known_values = {}
  while known_values.get('a') == None:
    for key, instruction in storage.items():
      if len(instruction) == 1:
        if represents_int(instruction[0]):
          known_values[key] = int(instruction[0])
          keys_to_remove.append(key)
          continue
        elif known_values.get(instruction[0]) != None:
          known_values[key] = known_values.get(instruction[0])
          keys_to_remove.append(key)
          continue

      if len(instruction) == 2:
        # Must be NOT instruction
        if instruction[0] != 'NOT':
          print(f'Error on: {instruction}')
          continue

        if represents_int(instruction[1]):
          known_values[key] = (~ int(instruction[1])) + 2**16
          keys_to_remove.append(key)
          continue
        elif known_values.get(instruction[1]) != None:
          known_values[key] = (~ known_values.get(instruction[1])) + 2**16
          keys_to_remove.append(key)
          continue

      if (represents_int(instruction[0]) or known_values.get(instruction[0])) != None \
        and (represents_int(instruction[2]) or known_values.get(instruction[2])) != None:
        a = int(instruction[0]) if represents_int(instruction[0]) else known_values.get(instruction[0])
        b = int(instruction[2]) if represents_int(instruction[2]) else known_values.get(instruction[2])
        
        if instruction[1] == 'AND':
          known_values[key] = a & b
          keys_to_remove.append(key)
          continue
        elif instruction[1] == 'OR':
          known_values[key] = a | b
          keys_to_remove.append(key)
          continue
        elif instruction[1] == 'LSHIFT':
          known_values[key] = a << b
          keys_to_remove.append(key)
          continue
        elif instruction[1] == 'RSHIFT':
          known_values[key] = a >> b
          keys_to_remove.append(key)
          continue
        else:
          print(f'Error on: {instruction}')

    if len(keys_to_remove) == 0:
      # Either unsolvable or there's a bug, we need to debug.
      import pdb; pdb.set_trace()

    for key in keys_to_remove:
      storage.pop(key)
    keys_to_remove = []

  return known_values.get('a')

def represents_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()
input_lines  = list(map(lambda line: line.rstrip(), input_lines))

solution_one = solution_one(input_lines)
solution_two = solution_two(input_lines, solution_one)

print(f'Solution One: {solution_one}')
print(f'Solution Two: {solution_two}')
