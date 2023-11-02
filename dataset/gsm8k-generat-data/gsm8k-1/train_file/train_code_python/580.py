def solution():
    """In ten years, I'll be twice my brother's age. The sum of our ages will then be 45 years old. How old am I now?"""
    sum_of_ages = 45
    age_difference = 10
    my_age_in_10_years = sum_of_ages / 3 + age_difference
    my_current_age = my_age_in_10_years - age_difference
    result = my_current_age
    return result

print(solution())