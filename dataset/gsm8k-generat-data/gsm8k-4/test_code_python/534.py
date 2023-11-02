def solution():
    """Jessica is six years older than Claire. In two years, Claire will be 20 years old. How old is Jessica now?"""
    # Define Claire's age in two years
    claire_future_age = 20

    # Calculate Claire's current age
    claire_current_age = claire_future_age - 2

    # Calculate Jessica's current age
    jessica_current_age = claire_current_age + 6

    # Return Jessica's current age
    result = jessica_current_age
    return result

print(solution())