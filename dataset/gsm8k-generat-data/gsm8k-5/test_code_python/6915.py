def solution():
    total_players = 1000  # A total of 1000 players signed up
    age_group_25_35 = 2/5 * total_players  # Exactly two-fifths of NBA players who signed up for a test are aged between 25 and 35 years
    age_group_older_35 = 3/8 * total_players  # Three-eighths of them are older than 35
    age_group_younger_25 = total_players - age_group_25_35 - age_group_older_35  # Calculate the number of players who are younger than 25 years
    result = age_group_younger_25
    return result

print(solution())