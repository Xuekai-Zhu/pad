def solution():
    """Xavier is twice as old as Yasmin is. Xavier will 30 years old in six years. What is the total of their ages now?"""
    # Define Xavier's age in six years
    xavier_six_years = 30

    # Calculate Xavier's current age
    xavier_age = xavier_six_years - 6

    # Calculate Yasmin's age
    yasmin_age = xavier_age / 2

    # Calculate the total of their ages
    total_age = xavier_age + yasmin_age

    # Return the result
    result = total_age
    return result

print(solution())