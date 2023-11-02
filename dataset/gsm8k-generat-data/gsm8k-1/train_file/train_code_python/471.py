def solution():
    """It takes 7 years for an apple tree to bear fruit. If Lydia planted a tree when she was 4 years old and is now 9 years old, how old would she be when she gets to eat an apple from her tree for the first time?"""
    years_until_fruit = 7
    age_when_planted = 4
    current_age = 9
    years_until_fruit_bearing = years_until_fruit - (current_age - age_when_planted)
    age_when_fruit_bearing = current_age + years_until_fruit_bearing
    result = age_when_fruit_bearing
    return result

print(solution())