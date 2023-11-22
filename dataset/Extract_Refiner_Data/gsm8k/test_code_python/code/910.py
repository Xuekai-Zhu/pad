def solution():
    
    # Define the number of tune-ups needed per mile
    TUNE_UPS_PER_MILE = 1000

    # Define the number of miles Jon drives per day and the number of days in a month
    MILES_PER_DAY = 100
    DAYS_PER_MONTH = 30

    # Calculate the total number of miles Jon drives in a month
    total_miles = MILES_PER_DAY * DAYS_PER_MONTH

    # Calculate the total number of tune-ups Jon needs in the month
    total_tune_ups = total_miles / TUNE_UPS_PER_MILE

    # Display the total number of tune-ups
    result = total_tune_ups
    return result

print(solution())