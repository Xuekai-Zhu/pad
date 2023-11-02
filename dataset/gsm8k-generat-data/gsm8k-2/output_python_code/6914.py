def solution():
    """Exactly two-fifths of NBA players who signed up for a test are aged between 25 and 35 years. If three-eighths of them are older than 35, and a total of 1000 players signed up, how many players are younger than 25 years?"""
    total_players = 1000
    age_25_35 = total_players * 2/5
    age_over_35 = total_players * 3/8
    age_under_25 = total_players - age_25_35 - age_over_35
    result = age_under_25
    return result

print(solution())