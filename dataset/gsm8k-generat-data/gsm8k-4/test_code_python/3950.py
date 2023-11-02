def solution():
    """A rival football team has won twice as many matches as the home team they will be playing did. If records show that the home team has won three matches, and each team drew four matches and lost none, how many matches have both teams played in total?"""
    # Define the number of wins for the home team
    home_wins = 3

    # Define the number of wins for the rival team
    rival_wins = home_wins * 2

    # Define the number of draws for both teams
    draws = 4

    # Calculate the total number of matches played by both teams
    total_matches = (home_wins + rival_wins + draws) * 2

    # return the result
    result = total_matches
    return result

print(solution())