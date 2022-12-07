LOSS = 0
TIE = 3
WIN = 6

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

def solution_one(input_lines):
  total_score = 0
  for line in input_lines:
    opponent, proposed = line.split(" ")
    proposed = proposed.strip()
    opponent = opponent.strip()

    if proposed == "X":
      total_score += 1

      if opponent == "A":
        total_score += TIE
      elif opponent == "B":
        total_score += LOSS
      elif opponent == "C":
        total_score += WIN

    elif proposed == "Y":
      total_score += 2

      if opponent == "A":
        total_score += WIN
      elif opponent == "B":
        total_score += TIE
      elif opponent == "C":
        total_score += LOSS

    elif proposed == "Z":
      total_score += 3

      if opponent == "A":
        total_score += LOSS
      elif opponent == "B":
        total_score += WIN
      elif opponent == "C":
        total_score += TIE

    else:
      print("INVALID " + proposed)

  return total_score

def solution_two(input_lines):
  total_score = 0
  for line in input_lines:
    opponent, outcome = line.split(" ")
    opponent = opponent.strip()
    outcome = outcome.strip()


    # ROCK
    if opponent == "A":
      if outcome == "X":
        total_score += LOSS
        total_score += SCISSORS_SCORE
      elif outcome == "Y":
        total_score += TIE
        total_score += ROCK_SCORE
      elif outcome == "Z":
        total_score += WIN
        total_score += PAPER_SCORE

    # PAPER
    elif opponent == "B":
      if outcome == "X":
        total_score += LOSS
        total_score += ROCK_SCORE
      elif outcome == "Y":
        total_score += TIE
        total_score += PAPER_SCORE
      elif outcome == "Z":
        total_score += WIN
        total_score += SCISSORS_SCORE

    # SCISSORS
    elif opponent == "C":
      if outcome == "X":
        total_score += LOSS
        total_score += PAPER_SCORE
      elif outcome == "Y":
        total_score += TIE
        total_score += SCISSORS_SCORE
      elif outcome == "Z":
        total_score += WIN
        total_score += ROCK_SCORE

  return total_score

input_stream = open('input.txt', 'r')
input_lines  = input_stream.readlines()

print(f'Solution One: {solution_one(input_lines)}')
print(f'Solution Two: {solution_two(input_lines)}')
