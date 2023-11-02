def solution():
    """The number of trees is three times more than the number of stones in the courtyard. There are also twice as many birds in the trees as the combined number of trees and stones in the yard. If the number of stones is 40, how many birds are in the trees?"""
    stones = 40
    trees = 3 * stones
    total = stones + trees
    birds = 2 * total
    result = birds
    return result

print(solution())