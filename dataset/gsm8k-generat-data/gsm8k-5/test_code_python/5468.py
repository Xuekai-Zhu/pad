def solution():
    total_trees = 8
    fruits_per_tree = 200
    fraction_picked = 2/5
    
    # Calculate the total number of oranges picked by Dulce
    total_picked = total_trees * fruits_per_tree * fraction_picked
    
    # Calculate the total number of oranges remaining
    total_remaining = total_trees * fruits_per_tree - total_picked
    result = total_remaining
    return result

print(solution())