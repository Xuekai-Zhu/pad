def solution():
    # Calculate the number of weeks in one month
    weeks_in_month = 4

    # Calculate the number of bikes added during the month
    bikes_added = 3 * weeks_in_month

    # Calculate the original number of bikes in stock
    original_bikes = bikes_added + 18 - 45  # subtract the number of bikes sold and the current number of bikes in stock
    result = original_bikes
    return result

print(solution())