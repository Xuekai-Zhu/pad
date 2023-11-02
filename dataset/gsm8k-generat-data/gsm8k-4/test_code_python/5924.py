def solution():
    """For every sandwich that he eats, Sam eats four apples. If he eats 10 sandwiches every day for one week, how many apples does he eat?"""
    # Define the number of sandwiches that Sam eats per day
    sandwiches_per_day = 10

    # Define the number of days in a week
    days_per_week = 7

    # Calculate the total number of sandwiches that Sam eats in a week
    sandwiches_per_week = sandwiches_per_day * days_per_week

    # Calculate the total number of apples that Sam eats in a week
    apples_per_week = sandwiches_per_week * 4

    # return the result
    result = apples_per_week
    return result

print(solution())