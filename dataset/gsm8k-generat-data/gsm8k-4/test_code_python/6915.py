def solution():
    """Exactly two-fifths of NBA players who signed up for a test are aged between 25 and 35 years. If three-eighths of them are older than 35, and a total of 1000 players signed up, how many players are younger than 25 years?"""
    # Define the total number of players
    total_players = 1000

    # Calculate the number of players aged 25-35
    middle_aged_players = total_players * (2/5)

    # Calculate the number of players older than 35
    old_players = total_players * (3/8)

    # Calculate the number of players younger than 25
    young_players = total_players - middle_aged_players - old_players

    # Return the result
    result = young_players
    return result

print(solution())