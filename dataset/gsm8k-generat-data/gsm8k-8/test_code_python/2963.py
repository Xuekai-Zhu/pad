def solution():
    # Define Kate's current age
    kate_age = 29

    # Calculate Tully's age three years from now
    tully_future_age = 2 * (kate_age + 3)

    # Calculate Tully's current age
    tully_current_age = tully_future_age - 3

    # Calculate Tully's age one year ago
    tully_past_age = tully_current_age - 1
    result = tully_past_age
    return result

print(solution())