def solution():
    
    alice_age = 20
    alice_pens = 60
    clara_pens = (2/5) * alice_pens
    clara_age_diff = alice_pens - clara_pens
    clara_age = alice_age + clara_age_diff
    clara_age_in_5_years = clara_age + 5
    result = clara_age_in_5_years
    return result

print(solution())