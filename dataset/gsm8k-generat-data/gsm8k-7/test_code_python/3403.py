def solution():
    # Calculate Will's current age
    will_age_now = 4 + 3  # Will was 4 years old 3 years ago
    # Calculate Diane's current age
    diane_age_now = will_age_now * 2

    # Calculate the sum of their ages in 5 years
    sum_of_ages_in_5_years = (will_age_now + 5) + (diane_age_now + 5)
    result = sum_of_ages_in_5_years
    return result

print(solution())