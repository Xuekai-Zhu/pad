def solution():
    sandwiches_per_day = 10
    days_per_week = 7
    apples_per_sandwich = 4

    # Calculate the total number of sandwiches that Sam eats in a week
    total_sandwiches = sandwiches_per_day * days_per_week

    # Calculate the total number of apples that Sam eats in a week
    total_apples = total_sandwiches * apples_per_sandwich
    result = total_apples
    return result

print(solution())