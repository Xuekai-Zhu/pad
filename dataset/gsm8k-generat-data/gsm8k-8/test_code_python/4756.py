def solution():
    # Calculate the difference in temperature
    temp_difference = 80 - 78.2

    # Calculate the number of trees needed to achieve the temperature drop
    trees_needed = temp_difference / 0.1

    # Calculate the cost of planting the trees
    cost_of_trees = trees_needed * 6

    result = cost_of_trees
    return result

print(solution())