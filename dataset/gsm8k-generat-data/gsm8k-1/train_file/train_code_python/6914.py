def solution():
    """Exactly two-fifths of NBA players who signed up for a test are aged between 25 and 35 years. If three-eighths of them
    are older than 35, and a total of 1000 players signed up, how many players are younger than 25 years?"""
    total_players = 1000
    two_fifths = 2/5
    three_eighths = 3/8
    
    # Calculate the number of players aged between 25 and 35
    between_25_35 = total_players * two_fifths
    
    # Calculate the number of players older than 35
    older_than_35 = total_players * three_eighths
    
    # Calculate the number of players younger than 25 by subtracting the number of players aged 25 to 35 and older than 35 from the total
    younger_than_25 = total_players - between_25_35 - older_than_35
    
    result = younger_than_25
    return result

print(solution())