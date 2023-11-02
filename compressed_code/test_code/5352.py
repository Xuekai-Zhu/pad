def solution():
    
    total_players = 1000
    age_25_35 = total_players * 2/5
    age_over_35 = total_players * 3/8
    age_under_25 = total_players - age_25_35 - age_over_35
    result = age_under_25
    return result

print(solution())