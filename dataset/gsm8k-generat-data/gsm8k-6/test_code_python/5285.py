def solution():
    # Calculate the number of trees in the courtyard
    trees = 3 * 40  # the number of trees is three times more than the number of stones in the courtyard

    # Calculate the combined number of trees and stones in the courtyard
    total_trees_stones = trees + 40

    # Calculate the number of birds in the trees
    birds = 2 * total_trees_stones  # twice as many birds in the trees as the combined number of trees and stones in the yard

    result = birds
    return result

print(solution())