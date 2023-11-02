def solution():
    """Nicki spent the last year running a lot. For the first half of the year, she ran a total of 20 miles per week. For the second half of the year, she increased the mileage to 30 miles per week. How many miles total did she run for the year?"""
    # Define the number of weeks in a year and the average weekly mileage
    WEEKS_IN_YEAR = 52
    AVERAGE_WEEKLY_MILEAGE = (20 + 30) / 2

    # Calculate the total mileage for the year
    total_mileage = WEEKS_IN_YEAR * AVERAGE_WEEKLY_MILEAGE

    # Display the total mileage
    result = total_mileage
    return result

print(solution())