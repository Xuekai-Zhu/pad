def solution():
    """Ahmed has 8 orange trees and four times as many apple trees in his orchard as Hassan. If Hassan has one apple tree and two orange trees, and they both have only apple and orange trees in their orchards, how many more trees are in Ahmed's orchard than in Hassan's?"""
    Hassan_apple_trees = 1
    Hassan_orange_trees = 2
    Ahmed_orange_trees = 8
    Ahmed_apple_trees = 4 * Hassan_apple_trees
    total_Hassan_trees = Hassan_apple_trees + Hassan_orange_trees
    total_Ahmed_trees = Ahmed_apple_trees + Ahmed_orange_trees
    difference = total_Ahmed_trees - total_Hassan_trees
    result = difference
    return result

print(solution())