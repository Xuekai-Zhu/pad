def solution():
    temperature_drop = 1.8  # The temperature dropped from 80 to 78.2
    temperature_drop_per_tree = 0.1  # The temperature drops 0.1 degree per tree planted
    trees_needed = temperature_drop / temperature_drop_per_tree  # Calculate the number of trees needed
    cost_per_tree = 6  # It costs $6 to plant one tree

    # Calculate the total cost to plant the necessary number of trees
    total_cost = trees_needed * cost_per_tree
    result = total_cost
    return result

print(solution())