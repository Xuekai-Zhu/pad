def solution():
    
    # Define the rate of pay per 10 minutes
    RATE_PER_10_MINUTES = 5

    # Define the number of minutes Susan works in half an hour
    MINUTES_PER_HOUR = 60 * 60

    # Calculate the total number of 10-minute intervals Susan works in half an hour
    intervals = MINUTES_PER_HOUR / 10

    # Calculate Susan's earnings for the online task
    earnings = intervals * RATE_PER_10_MINUTES

    # Display Susan's earnings
    result = earnings
    return result

print(solution())