def solution():
    """Damien jogs 5 miles per day on weekdays only. How many miles does he run over three weeks?"""
    # Define the number of weekdays in a week
    WEEKDAYS = 5

    # Define the number of weeks
    weeks = 3

    # Calculate the total number of miles Damien runs
    total_miles = WEEKDAYS * 5 * weeks

    # Display the total number of miles Damien runs
    result = total_miles
    return result

print(solution())