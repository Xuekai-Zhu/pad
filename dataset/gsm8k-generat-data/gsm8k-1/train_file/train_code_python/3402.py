def solution():
    """Diane is twice as old as her brother, Will. If Will was 4 years old 3 years ago, what will the sum of their ages be in 5 years?"""
    will_age = 4 + 3  # Will's age now is 3 years more than 4 years (3 years ago)
    diane_age = will_age * 2  # Diane is twice as old as Will
    sum_of_ages_in_5_years = will_age + 5 + (diane_age + 5)
    result = sum_of_ages_in_5_years
    return result

print(solution())