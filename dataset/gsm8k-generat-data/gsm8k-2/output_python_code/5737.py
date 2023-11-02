def solution():
    """A soccer team has three goalies and ten defenders. The team also has twice as many midfielders as defenders, and the rest of the players are strikers. If the team has 40 players, how many strikers are in the team?"""
    total_players = 40
    goalies = 3
    defenders = 10
    midfielders = 2 * defenders
    remaining_players = total_players - goalies - defenders - midfielders
    strikers = remaining_players
    result = strikers
    return result

print(solution())