def solution():
    sandwiches_per_day = 10  # Sam eats 10 sandwiches per day
    days_per_week = 7  # Sam wants to know how many apples he eats in one week

    # Calculate the total number of sandwiches Sam eats in one week
    total_sandwiches = sandwiches_per_day * days_per_week

    # Calculate the total number of apples Sam eats in one week
    total_apples = 4 * total_sandwiches
    result = total_apples
    return result

print(solution())