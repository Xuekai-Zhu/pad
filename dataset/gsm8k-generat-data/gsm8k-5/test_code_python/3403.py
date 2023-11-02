def solution():
    # Calculate Will's current age
    will_age_now = 4 + 3  # Will was 4 years old 3 years ago, so now he is 7 years old

    # Calculate Diane's current age
    diane_age_now = 2 * will_age_now  # Diane is twice as old as Will

    # Calculate the sum of their ages in 5 years
    sum_in_5_years = will_age_now + 5 + diane_age_now + 5
    result = sum_in_5_years
    return result

print(solution())