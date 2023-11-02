def solution():
    """Dulce's father has eight orange trees on his farm. If each tree has 200 fruits and Dulce picks 2/5 of the oranges from each tree, calculate the total number of fruits remaining in all the trees."""
    # Define the number of trees and fruits per tree
    NUM_TREES = 8
    FRUITS_PER_TREE = 200

    # Calculate the number of fruits picked by Dulce from each tree
    num_picked_per_tree = int(2/5 * FRUITS_PER_TREE)

    # Calculate the number of fruits remaining on each tree
    num_remaining_per_tree = FRUITS_PER_TREE - num_picked_per_tree

    # Calculate the total number of fruits remaining on all the trees
    total_remaining_fruits = NUM_TREES * num_remaining_per_tree

    # Display the total number of fruits remaining
    result = total_remaining_fruits
    return result

print(solution())