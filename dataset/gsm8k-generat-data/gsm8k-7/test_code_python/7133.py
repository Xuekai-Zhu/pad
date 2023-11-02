def solution():
    num_apples_per_bag = 15
    num_apples_left = 60
    num_apples_eaten = 4 * 2
    num_apples_sold = 7

    # Calculate the total number of apples collected by the children
    total_apples_collected = num_apples_per_bag * num_children

    # Calculate the total number of apples that were not eaten or sold
    total_apples_left = num_apples_collected - num_apples_eaten - num_apples_sold

    # Calculate the number of children
    num_children = total_apples_left / num_apples_per_bag
    result = num_children
    return result

print(solution())