def solution():
    
    alice_age = 20
    alice_pens = 60
    clara_pens = (2/5)*alice_pens
    pen_difference = alice_pens - clara_pens
    age_difference = pen_difference
    clara_age = alice_age + age_difference
    
    
    clara_age_in_5_years = clara_age + 5
    
    return clara_age_in_5_years

print(solution())