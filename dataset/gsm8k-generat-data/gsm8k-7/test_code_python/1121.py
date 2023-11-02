def solution():
    alice_pens = 60
    alice_age = 20
    clara_pens = (2/5) * alice_pens
    clara_age_diff = alice_pens - clara_pens
    clara_age = alice_age + clara_age_diff
    
    # Calculate Clara's age in 5 years
    clara_age_in_5_years = clara_age + 5
    result = clara_age_in_5_years
    return result

print(solution())