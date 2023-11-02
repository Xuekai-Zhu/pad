def solution():
    """Stanley sold 4 cups of lemonade an hour. His brother, Carl, sold 7 cups of lemonade an hour. How many more cups did Carl sell than Stanley in 3 hours?"""
    # Define the number of cups Stanley sold per hour and the number of cups Carl sold per hour
    stanley_cups_per_hour = 4
    carl_cups_per_hour = 7

    # Calculate the total number of cups Stanley sold in 3 hours
    stanley_total_cups = stanley_cups_per_hour * 3

    # Calculate the total number of cups Carl sold in 3 hours
    carl_total_cups = carl_cups_per_hour * 3

    # Calculate the difference in the total number of cups sold between Carl and Stanley in 3 hours
    cups_difference = carl_total_cups - stanley_total_cups

    # return the result
    result = cups_difference
    return result

print(solution())