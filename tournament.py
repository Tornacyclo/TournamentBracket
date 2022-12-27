# define the number of teams in the tournament
num_teams = 8

# generate a list of team names (for this example, we will just use numbers)
teams = [str(i) for i in range(1, num_teams + 1)]

# initialize the bracket as a dictionary with keys for each round and values as lists of tuples
bracket = {1: [(teams[i], teams[num_teams - i - 1]) for i in range(num_teams // 2)]}

# initialize the current round and the number of teams remaining in the tournament
current_round = 2
num_teams_remaining = num_teams // 2

# generate the rest of the bracket
while num_teams_remaining > 1:
  bracket[current_round] = []
  for i in range(num_teams_remaining // 2):
    bracket[current_round].append((None, None))
  num_teams_remaining = num_teams_remaining // 2
  current_round += 1

# display the bracket
for round, match ups in bracket.items():
  print(f"Round {round}:")
  for match in match ups:
    print(f"  {match[0]} vs {match[1]}")
