def solution():
    regular_bread_per_sandwich = 2  # Two pieces of bread for one regular sandwich
    doublemeat_bread_per_sandwich = 3  # Three pieces of bread for one double meat sandwich
    num_regular_sandwiches = 14  # 14 regular sandwiches
    num_doublemeat_sandwiches = 12  # 12 double meat sandwiches

    # Calculate the total number of bread pieces needed for regular sandwiches
    regular_bread_total = num_regular_sandwiches * regular_bread_per_sandwich

    # Calculate the total number of bread pieces needed for double meat sandwiches
    doublemeat_bread_total = num_doublemeat_sandwiches * doublemeat_bread_per_sandwich

    # Calculate the total number of bread pieces needed for all sandwiches
    total_bread = regular_bread_total + doublemeat_bread_total
    result = total_bread
    return result

print(solution())