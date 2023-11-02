def solution():
    
    fourth_grade_trees = 30
    fifth_grade_trees = 2 * fourth_grade_trees
    sixth_grade_trees = 3 * fifth_grade_trees - 30
    total_trees_planted = fourth_grade_trees + fifth_grade_trees + sixth_grade_trees
    result = total_trees_planted
    return result

print(solution())