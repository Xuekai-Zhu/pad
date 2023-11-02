def solution():
    """40 less than 10 times Diaz's age is 20 more than 10 times Sierra's age. If Sierra is currently 30 years old, how old will Diaz be 20 years from now?"""
    # Determine Sierra's age
    sierra_age = 30

    # Calculate the age difference between Diaz and Sierra
    age_diff = (40 + 10 * sierra_age - 20) / 10

    # Calculate Diaz's current age
    diaz_age = 10 * sierra_age - age_diff

    # Calculate Diaz's age 20 years from now
    diaz_future_age = diaz_age + 20

    # Display Diaz's age 20 years from now
    result = diaz_future_age
    return result

print(solution())