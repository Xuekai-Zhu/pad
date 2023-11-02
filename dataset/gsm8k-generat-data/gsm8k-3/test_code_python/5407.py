def solution():
    """Jill has a difficult test to study for.  She decides to study one day for 2 hours.  The next day she doubles this amount, and the day after that she studies one hour less than the previous day.  How many minutes does Jill study over the 3 days?"""
    # Define the number of hours Jill studies on the first day
    hours_day_1 = 2

    # Calculate the number of hours Jill studies on the second day
    hours_day_2 = hours_day_1 * 2

    # Calculate the number of hours Jill studies on the third day
    hours_day_3 = hours_day_2 - 1

    # Calculate the total number of minutes Jill studies over the 3 days
    total_minutes = (hours_day_1 + hours_day_2 + hours_day_3) * 60

    # Display the total number of minutes Jill studies
    result = total_minutes
    return result

print(solution())