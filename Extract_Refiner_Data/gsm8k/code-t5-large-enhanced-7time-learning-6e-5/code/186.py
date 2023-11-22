def solution():
    
    # Define the number of minutes in 3 hours
    MINUTES_IN_3_HOURS = 60 * 60

    # Define the number of peaches John can collect in 1 minute
    PEACHES_PER_MINUTE = 2

    # Calculate the total number of peaches John collects
    total_peaches = MINUTES_IN_3_HOURS * PEACHES_PER_MINUTE

    # Display the total number of peaches
    result = total_peaches
    return result

print(solution())