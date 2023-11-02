def solution():
    trees_planted_4th_grade = 30
    trees_planted_5th_grade = 2 * trees_planted_4th_grade
    trees_planted_6th_grade = 3 * trees_planted_5th_grade - 30
    total_trees_planted = trees_planted_4th_grade + trees_planted_5th_grade + trees_planted_6th_grade
    
    result = total_trees_planted
    return result

print(solution())