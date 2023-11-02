def solution():
    """A soccer team has three goalies and ten defenders. The team also has twice as many midfielders as defenders, and the rest of the players are strikers. If the team has 40 players, how many strikers are in the team?"""
    num_goalies = 3
    num_defenders = 10
    num_midfielders = 2 * num_defenders
    num_players = 40
    num_strikers = num_players - (num_goalies + num_defenders + num_midfielders)
    result = num_strikers
    return result

print(solution())