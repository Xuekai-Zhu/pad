def solution():
    """Summer performs 5 sun salutation yoga poses as soon as she gets out of bed, on the weekdays.  How many sun salutations will she perform throughout an entire year?"""
    # Define the number of sun salutations performed on a typical weekday
    SUN_SALUTATIONS_PER_WEEKDAY = 5

    # Calculate the total number of sun salutations in a year
    weekdays_in_year = 5 * 52  # 5 weekdays per week for 52 weeks
    total_sun_salutations = SUN_SALUTATIONS_PER_WEEKDAY * weekdays_in_year

    # Display the total number of sun salutations
    result = total_sun_salutations
    return result

print(solution())