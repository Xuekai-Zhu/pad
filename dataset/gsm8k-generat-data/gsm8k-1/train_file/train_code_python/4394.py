def solution():
    """Xavier is twice as old as Yasmin is. Xavier will 30 years old in six years. What is the total of their ages now?"""
    xavier_age_in_6_years = 30
    yasmin_age_in_6_years = xavier_age_in_6_years / 2
    current_age_difference = xavier_age_in_6_years - 6 - (yasmin_age_in_6_years - 6)
    current_xavier_age = xavier_age_in_6_years - 6
    current_yasmin_age = current_xavier_age - current_age_difference
    total_age = current_xavier_age + current_yasmin_age
    result = total_age
    return result

print(solution())