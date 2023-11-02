def solution():
    """Dulce's father has eight orange trees on his farm. If each tree has 200 fruits and Dulce picks 2/5 of the oranges from each tree, calculate the total number of fruits remaining in all the trees."""
    num_trees = 8
    num_fruits_per_tree = 200
    fraction_picked = 2/5
    total_fruits_remaining = num_trees * num_fruits_per_tree * (1 - fraction_picked)
    result = total_fruits_remaining
    return result

print(solution())