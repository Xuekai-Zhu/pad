def solution():
    """Xavier is twice as old as Yasmin is. Xavier will 30 years old in six years. What is the total of their ages now?"""
    xavier_age_in_6_years = 30
    xavier_age_now = xavier_age_in_6_years - 6
    yasmin_age_now = xavier_age_now / 2
    total_age = xavier_age_now + yasmin_age_now
    result = total_age
    return result

print(solution())