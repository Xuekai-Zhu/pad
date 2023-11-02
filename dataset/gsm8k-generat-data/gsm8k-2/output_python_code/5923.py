def solution():
    """For every sandwich that he eats, Sam eats four apples. If he eats 10 sandwiches every day for one week, how many apples does he eat?"""
    sandwiches_per_day = 10
    apples_per_sandwich = 4
    days_per_week = 7
    total_sandwiches = sandwiches_per_day * days_per_week
    total_apples = total_sandwiches * apples_per_sandwich
    result = total_apples
    return result

print(solution())