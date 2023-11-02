def solution():
    num_leaves_thursday = 12
    num_leaves_friday = 13
    brown_leaves_percentage = 0.2
    green_leaves_percentage = 0.2

    # Calculate the total number of leaves Bronson collects
    total_leaves = num_leaves_thursday + num_leaves_friday

    # Calculate the number of brown leaves
    num_brown_leaves = int(total_leaves * brown_leaves_percentage)

    # Calculate the number of green leaves
    num_green_leaves = int(total_leaves * green_leaves_percentage)

    # Calculate the number of yellow leaves
    num_yellow_leaves = total_leaves - num_brown_leaves - num_green_leaves
    result = num_yellow_leaves
    return result

print(solution())