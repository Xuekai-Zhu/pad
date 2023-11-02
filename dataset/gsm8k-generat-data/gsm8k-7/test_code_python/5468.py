def solution():
    num_trees = 8
    num_fruits_per_tree = 200
    fraction_picked = 2/5

    # Calculate the total number of fruits picked by Dulce
    total_picked = num_trees * num_fruits_per_tree * fraction_picked

    # Calculate the total number of fruits remaining in all trees
    total_remaining = (num_trees * num_fruits_per_tree) - total_picked
    result = total_remaining
    return result

print(solution())