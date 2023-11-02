def solution():
    """A bicycle shop owner adds 3 bikes to her stock every week. After 1 month, she had sold 18 bikes but still had 45 bikes in stock. How many bikes did she have originally?"""
    # Define the number of weeks in a month and the number of bikes added per week
    WEEKS_IN_MONTH = 4
    BIKES_ADDED_PER_WEEK = 3

    # Calculate the total number of bikes added in a month
    total_bikes_added = WEEKS_IN_MONTH * BIKES_ADDED_PER_WEEK

    # Calculate the original number of bikes
    original_num_bikes = total_bikes_added + 45 - 18

    # return the result
    result = original_num_bikes
    return result

print(solution())