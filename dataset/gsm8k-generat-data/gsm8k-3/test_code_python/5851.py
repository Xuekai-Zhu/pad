def solution():
    """Gilbert, the bearded dragon, eats 4 crickets per week when the temperature averages 90 degrees F per day, but he eats twice as many crickets per week when the temperature averages 100 degrees F.  How many crickets will he eat over 15 weeks if the temperature averages 90 degrees F for 80% of the time, and 100 degrees F for the remainder of the time?"""
    # Define the number of crickets Gilbert eats at 90 degrees F
    CRICKETS_90 = 4

    # Define the number of crickets Gilbert eats at 100 degrees F
    CRICKETS_100 = 2 * CRICKETS_90

    # Define the percentage of time Gilbert is at 90 degrees F
    PERCENT_90 = 0.8

    # Define the percentage of time Gilbert is at 100 degrees F
    PERCENT_100 = 1 - PERCENT_90

    # Define the number of weeks Gilbert is monitored
    WEEKS = 15

    # Calculate the number of crickets Gilbert eats at 90 degrees F
    crickets_90 = CRICKETS_90 * (PERCENT_90 * 7 * WEEKS)

    # Calculate the number of crickets Gilbert eats at 100 degrees F
    crickets_100 = CRICKETS_100 * (PERCENT_100 * 7 * WEEKS)

    # Calculate the total number of crickets Gilbert eats
    total_crickets = crickets_90 + crickets_100

    # Display the total number of crickets
    result = total_crickets
    return result

print(solution())