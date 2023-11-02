def solution():
    temperature_drop_per_tree = 0.1
    cost_per_tree = 6
    initial_temperature = 80
    final_temperature = 78.2

    # Calculate the total temperature drop needed
    total_temperature_drop = initial_temperature - final_temperature

    # Calculate the number of trees needed to achieve the temperature drop
    num_trees = total_temperature_drop / temperature_drop_per_tree

    # Calculate the total cost of planting all the trees
    total_cost = num_trees * cost_per_tree
    result = total_cost
    return result

print(solution())