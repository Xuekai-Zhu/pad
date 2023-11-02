def solution():
    
    years_until_fruit = 7
    age_when_planted = 4
    current_age = 9
    years_until_fruit_bearing = years_until_fruit - (current_age - age_when_planted)
    age_when_fruit_bearing = current_age + years_until_fruit_bearing
    result = age_when_fruit_bearing
    return result

print(solution())