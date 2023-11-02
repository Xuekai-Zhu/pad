def solution():
    num_regular_sandwiches = 14
    num_double_meat_sandwiches = 12

    # Calculate the total number of pieces of bread needed for regular sandwiches
    bread_for_regular = 2 * num_regular_sandwiches

    # Calculate the total number of pieces of bread needed for double meat sandwiches
    bread_for_double_meat = 3 * num_double_meat_sandwiches

    # Calculate the total number of pieces of bread needed
    total_bread = bread_for_regular + bread_for_double_meat

    result = total_bread
    return result

print(solution())