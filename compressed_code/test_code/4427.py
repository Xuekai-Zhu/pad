def solution():
    
    marbles = 100
    gideon_age_in_5_years = (marbles * (1 - 3/4)) * 2
    gideon_current_age = gideon_age_in_5_years - 5
    result = gideon_current_age
    return result

print(solution())