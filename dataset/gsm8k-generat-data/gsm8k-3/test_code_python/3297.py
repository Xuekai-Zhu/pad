def solution():
    """Tom's puts 30 miles per day on his bike for the first 183 days of the year.  For the rest of the days of the year he goes 35 miles per day.  How many miles does he drive for the year?"""
    # Define the number of days and miles per day for each period
    FIRST_PERIOD_DAYS = 183
    FIRST_PERIOD_MILES = 30
    SECOND_PERIOD_DAYS = 182
    SECOND_PERIOD_MILES = 35

    # Calculate the total miles for the first period
    first_period_miles = FIRST_PERIOD_DAYS * FIRST_PERIOD_MILES

    # Calculate the total miles for the second period
    second_period_miles = SECOND_PERIOD_DAYS * SECOND_PERIOD_MILES

    # Calculate the total miles for the year
    total_miles = first_period_miles + second_period_miles

    # Display the total miles
    result = total_miles
    return result

print(solution())