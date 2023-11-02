def solution():
    """Sasha heard that planting trees helps to reduce the local temperature. For each tree planted, the temperature drops .1 degree. A tree costs $6 to plant. If she got the local temperature to drop from 80 to 78.2, how much did it cost to plant the trees?"""
    temp_drop = 1.8
    temp_drop_per_tree = 0.1
    trees_needed = temp_drop / temp_drop_per_tree
    cost_per_tree = 6
    total_cost = trees_needed * cost_per_tree
    result = total_cost
    return result

print(solution())