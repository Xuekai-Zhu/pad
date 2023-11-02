def solution():
    """Sasha heard that planting trees helps to reduce the local temperature. For each tree planted, the temperature drops .1 degree. A tree costs $6 to plant. If she got the local temperature to drop from 80 to 78.2, how much did it cost to plant the trees?"""
    degrees_dropped = 1.8
    trees_planted = degrees_dropped / 0.1
    cost_per_tree = 6
    total_cost = trees_planted * cost_per_tree
    result = total_cost
    return result

print(solution())