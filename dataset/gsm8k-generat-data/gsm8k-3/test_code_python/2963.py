def solution():
    """Three years from now, Tully will be twice as old as Kate. How old was Tully a year ago if Kate is now 29 years old?"""
    # Calculate Tully's age three years from now
    tully_future_age = 2 * (29 + 3)

    # Calculate Tully's current age
    tully_current_age = tully_future_age - 3

    # Calculate Tully's age one year ago
    tully_past_age = tully_current_age - 1

    # Display Tully's age one year ago
    result = tully_past_age
    return result

print(solution())