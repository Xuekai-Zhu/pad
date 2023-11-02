def solution():
    """Mandy is 3 years old. Her brother is 4 times as old as she is. Her sister is 5 years younger than her brother. What is the age difference between Mandy and her sister?"""
    mandy_age = 3
    brother_age = mandy_age * 4
    sister_age = brother_age - 5
    age_difference = sister_age - mandy_age
    result = age_difference
    return result

print(solution())