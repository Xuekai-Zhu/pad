def solution():
    """A rival football team has won twice as many matches as the home team they will be playing did. If records show that the home team has won three matches, and each team drew four matches and lost none, how many matches have both teams played in total?"""
    # Calculate the number of matches the rival team has won
    rival_wins = 3 * 2

    # Calculate the total number of matches played by both teams
    total_matches = (3 + rival_wins + 4) * 2

    # Display the total number of matches played
    result = total_matches
    return result

print(solution())