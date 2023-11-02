def solution():
    """A rival football team has won twice as many matches as the home team they will be playing did. If records show that the home team has won three matches, and each team drew four matches and lost none, how many matches have both teams played in total?"""
    home_wins = 3
    rival_wins = home_wins * 2
    draws = 4
    losses = 0
    total_matches = (home_wins + rival_wins + draws + losses) * 2 # multiply by 2 to get the total for both teams
    result = total_matches
    return result

print(solution())