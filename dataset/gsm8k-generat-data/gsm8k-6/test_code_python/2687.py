def solution():
    # Calculate the total number of trees planted by the forester
    total_trees = 30  # initial number of trees
    total_trees *= 3  # triple total trees by planting new trees on Monday
    total_trees += (total_trees/3)  # add the number of trees planted on Tuesday (one-third of Monday's planting)
    result = total_trees - 30  # subtract the initial number of trees to get the total number planted
    return result

print(solution())