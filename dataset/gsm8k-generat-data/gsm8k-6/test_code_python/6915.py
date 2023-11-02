def solution():
    total_players = 1000  # total players signed up for the test
    age_25_35_players = (2/5) * total_players  # players aged between 25 and 35
    age_35_above_players = (3/8) * total_players  # players older than 35
    age_below_25_players = total_players - age_25_35_players - age_35_above_players  # players younger than 25
    result = age_below_25_players
    return result

print(solution())