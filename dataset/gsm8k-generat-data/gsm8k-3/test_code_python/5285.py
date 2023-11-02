def solution():
    """The number of trees is three times more than the number of stones in the courtyard. There are also twice as many birds in the trees as the combined number of trees and stones in the yard. If the number of stones is 40, how many birds are in the trees?"""
    # Define the number of stones
    stones = 40

    # Calculate the number of trees
    trees = 3 * stones

    # Calculate the combined number of trees and stones
    tree_stone_total = trees + stones

    # Calculate the number of birds
    birds = 2 * tree_stone_total

    # Display the number of birds
    result = birds
    return result

print(solution())