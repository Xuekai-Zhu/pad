def solution():
    # Calculate the total number of oranges picked
    total_oranges = 15 + 12 + (3 * (15 + 12))  # Betty picked 15, Bill picked 12, Frank picked 3 times the amount Betty and Bill picked

    # Calculate the total number of trees Frank planted
    total_trees = total_oranges * 2  # Frank planted 2 seeds from each orange

    # Calculate the total number of oranges Philip can pick
    total_philip_oranges = total_trees * 5  # Each tree has 5 oranges

    result = total_philip_oranges
    return result

print(solution())