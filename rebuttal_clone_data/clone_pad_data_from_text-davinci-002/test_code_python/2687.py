def solution():
    trees_planted_on_monday = 30 * 3
    trees_planted_on_tuesday = trees_planted_on_monday / 3
    total_trees_planted = trees_planted_on_monday + trees_planted_on_tuesday
    result = total_trees_planted
    return result

print(solution())