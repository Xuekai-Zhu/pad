def solution():
    # Calculate the total number of trees planted by all grades
    trees_planted_by_4th_graders = 30
    trees_planted_by_5th_graders = 2 * trees_planted_by_4th_graders
    trees_planted_by_6th_graders = 3 * trees_planted_by_5th_graders - 30
    total_trees_planted = trees_planted_by_4th_graders + trees_planted_by_5th_graders + trees_planted_by_6th_graders
    result = total_trees_planted
    return result

print(solution())