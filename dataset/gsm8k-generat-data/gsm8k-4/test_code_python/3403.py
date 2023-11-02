def solution():
    """Diane is twice as old as her brother, Will. If Will was 4 years old 3 years ago, what will the sum of their ages be in 5 years?"""
    # Define Will's age 3 years ago
    will_age_3years_ago = 4

    # Calculate Will's current age
    will_age = will_age_3years_ago + 3 + 5

    # Calculate Diane's current age
    diane_age = will_age * 2

    # Calculate the sum of their ages in 5 years
    sum_of_ages_in_5_years = diane_age + will_age + 5 + 5

    result = sum_of_ages_in_5_years
    return result

print(solution())