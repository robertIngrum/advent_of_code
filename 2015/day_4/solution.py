import hashlib

def solution_one(input_string):
  solution = None
  index    = 1
  while solution == None:
    string    = ("%s%s" % (input_string, index)).encode('utf-8')
    hexstring = hashlib.md5(string).hexdigest()

    if hexstring[0:5] == '00000':
      solution = index

    index += 1

  return solution

def solution_two(input_string):
  solution = None
  index    = 1
  while solution == None:
    string    = ("%s%s" % (input_string, index)).encode('utf-8')
    hexstring = hashlib.md5(string).hexdigest()

    if hexstring[0:6] == '000000':
      solution = index

    index += 1

  return solution

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()
input_string = input_lines[0].rstrip()

print(f'Solution One: {solution_one(input_string)}')
print(f'Solution Two: {solution_two(input_string)}')
