def solution():
    """Gilbert, the bearded dragon, eats 4 crickets per week when the temperature averages 90 degrees F per day, but he eats twice as many crickets per week when the temperature averages 100 degrees F. How many crickets will he eat over 15 weeks if the temperature averages 90 degrees F for 80% of the time, and 100 degrees F for the remainder of the time?"""
    # Define the average temperature and crickets eaten for each temperature
    temp_90 = 90
    temp_100 = 100
    crickets_90 = 4
    crickets_100 = 8

    # Calculate the number of weeks at each temperature
    weeks_90 = 0.8 * 15
    weeks_100 = 0.2 * 15

    # Calculate the total number of crickets eaten
    total_crickets = (weeks_90 * crickets_90) + (weeks_100 * crickets_100)

    result = total_crickets
    return result

print(solution())