def solution():
    """Dulce's father has eight orange trees on his farm. If each tree has 200 fruits and Dulce picks 2/5 of the oranges from each tree, calculate the total number of fruits remaining in all the trees."""
    # Define the number of trees and the number of oranges per tree
    num_trees = 8
    oranges_per_tree = 200

    # Calculate the total number of oranges picked by Dulce
    picked_oranges = (2/5) * oranges_per_tree * num_trees

    # Calculate the total number of oranges remaining on the trees
    remaining_oranges = oranges_per_tree * num_trees - picked_oranges

    # Return the result
    result = remaining_oranges
    return result

print(solution())