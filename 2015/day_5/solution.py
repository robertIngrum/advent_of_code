import re

def solution_one(input_lines):
  count = 0

  for word in input_lines:
    vowel_count = len(re.findall('[aeiou]',       word))
    pair_count  = len(re.findall(r'(\w)\1{1,}',   word))
    bad_strings = len(re.findall('(ab|cd|pq|xy)', word))
    ruling      = vowel_count >= 3 and pair_count >= 1 and bad_strings == 0

    # print(f'{word} - {ruling} - {vowel_count} - {pair_count} - {bad_strings}')

    if ruling == True:
      count += 1

  return count

def solution_two(input_lines):
  count = 0

  for word in input_lines:
    repeat_pair   = None
    spaced_repeat = None

    for char_index in range(0, len(word)):
      # For repeat pair
      if repeat_pair == None and char_index + 1 < len(word):
        target_str = word[char_index:char_index + 2:]
        search_str = word[0:char_index:] + '--' + word[char_index + 2::]

        if target_str in search_str:
          repeat_pair = target_str

      # For spaced repeat
      if spaced_repeat == None and char_index + 2 < len(word):
        if word[char_index] == word[char_index + 2]:
          spaced_repeat = word[char_index]

    # print(f'{word} - {repeat_pair} - {spaced_repeat}')

    if repeat_pair != None and spaced_repeat != None:
      count += 1

  return count

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()
input_lines = list(map(lambda num: num.rstrip(), input_lines))

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
