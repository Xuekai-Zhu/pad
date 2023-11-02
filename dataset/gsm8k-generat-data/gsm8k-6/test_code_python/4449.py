def solution():
    # Find the number of apple trees in Ahmed's orchard
    apple_trees = 4 * (2 + 1)  # four times as many apple trees as Hassan, who has 1 apple tree and 2 orange trees

    # Find the total number of trees in Ahmed's orchard
    total_trees_Ahmed = 8 + apple_trees

    # Find the total number of trees in Hassan's orchard
    total_trees_Hassan = 2 + 1  # 2 orange trees and 1 apple tree

    # Calculate the difference in the number of trees between the two orchards
    difference = total_trees_Ahmed - total_trees_Hassan
    result = difference
    return result

print(solution())