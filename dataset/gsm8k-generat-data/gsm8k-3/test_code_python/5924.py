def solution():
    """For every sandwich that he eats, Sam eats four apples. If he eats 10 sandwiches every day for one week, how many apples does he eat?"""
    # Define the number of sandwiches Sam eats per day and the number of days in a week
    SANDWICHES_PER_DAY = 10
    DAYS_PER_WEEK = 7

    # Calculate the total number of sandwiches Sam eats in a week
    sandwiches_per_week = SANDWICHES_PER_DAY * DAYS_PER_WEEK

    # Calculate the total number of apples Sam eats in a week
    apples_per_sandwich = 4
    apples_per_week = sandwiches_per_week * apples_per_sandwich

    # Display the total number of apples
    result = apples_per_week
    return result

print(solution())