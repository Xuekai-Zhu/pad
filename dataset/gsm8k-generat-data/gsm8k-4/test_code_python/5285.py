def solution():
    """The number of trees is three times more than the number of stones in the courtyard. There are also twice as many birds in the trees as the combined number of trees and stones in the yard. If the number of stones is 40, how many birds are in the trees?"""
    # Define the number of stones in the courtyard
    stones = 40

    # Calculate the number of trees, which is 3 times more than the number of stones
    trees = stones * 3

    # Calculate the combined number of trees and stones
    total_trees_and_stones = trees + stones

    # Calculate the number of birds in the trees, which is twice the combined number of trees and stones
    birds = total_trees_and_stones * 2

    # return the result
    result = birds
    return result

print(solution())