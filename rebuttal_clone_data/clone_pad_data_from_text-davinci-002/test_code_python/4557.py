def solution():
    trees_in_grove = 50 * 30
    normal_lemons_per_tree = 60
    improved_lemons_per_tree = normal_lemons_per_tree * 1.5
    total_normal_lemons = trees_in_grove * normal_lemons_per_tree
    total_improved_lemons = trees_in_grove * improved_lemons_per_tree
    total_lemons = total_normal_lemons + total_improved_lemons
    result = total_lemons
    return result

print(solution())