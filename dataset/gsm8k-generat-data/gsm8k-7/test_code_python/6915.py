def solution():
    total_players = 1000
    age_25_35_ratio = 2/5
    older_than_35_ratio = 3/8

    # Calculate number of players aged 25-35
    age_25_35 = total_players * age_25_35_ratio

    # Calculate number of players older than 35
    older_than_35 = total_players * older_than_35_ratio

    # Calculate number of players younger than 25
    younger_than_25 = total_players - age_25_35 - older_than_35
    result = younger_than_25
    return result

print(solution())