def solution():
    # Define the number of apples collected by each child
    apples_per_child = 15

    # Define the number of apples eaten or sold by some children
    total_eaten_or_sold = 2 * 4 + 7

    # Calculate the number of children
    total_apples_left = 60
    total_apples_collected = apples_per_child * num_children
    num_children = (total_apples_collected - total_eaten_or_sold - total_apples_left) / apples_per_child

    result = num_children
    return result

print(solution())