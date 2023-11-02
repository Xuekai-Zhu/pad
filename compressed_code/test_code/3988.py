def solution():
    
    thomas_age = 6
    sister_age = thomas_age + 13
    brother_age = sister_age + 5
    age_difference = brother_age - thomas_age
    james_age_at_thomas_current_age = brother_age + age_difference
    result = james_age_at_thomas_current_age
    return result

print(solution())