def solution():
    """Summer performs 5 sun salutation yoga poses as soon as she gets out of bed, on the weekdays. How many sun salutations will she perform throughout an entire year?"""
    # Define the number of sun salutations per weekday and the number of weekdays in a year
    SUN_SALUTATIONS_PER_WEEKDAY = 5
    WEEKDAYS_PER_YEAR = 5 * 52

    # Calculate the total number of sun salutations in a year
    total_sun_salutations = SUN_SALUTATIONS_PER_WEEKDAY * WEEKDAYS_PER_YEAR

    # Return the result
    result = total_sun_salutations
    return result

print(solution())