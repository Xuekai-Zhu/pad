def solution():
    # Calculate Gladys' current age
    gladys_current_age = 40 - 10  # Gladys will be 40 years old ten years from now
    # Calculate half of Gladys' current age
    half_gladys_current_age = gladys_current_age / 2
    # Calculate Juanico's current age
    juanico_current_age = half_gladys_current_age - 4

    # Calculate Juanico's age 30 years from now
    juanico_future_age = juanico_current_age + 30
    result = juanico_future_age
    return result

print(solution())