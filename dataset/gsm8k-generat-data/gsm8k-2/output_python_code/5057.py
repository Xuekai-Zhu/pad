def solution():
    """A school does a yearly tree planting activity. This year, the 4th graders planted a total of 30 trees while 5th graders planted twice as many. The 6th graders planted 30 fewer than thrice the number of trees planted by the 5th graders. How many trees did they plant altogether?"""
    fourth_grade_trees = 30
    fifth_grade_trees = 2 * fourth_grade_trees
    sixth_grade_trees = 3 * fifth_grade_trees - 30
    total_trees_planted = fourth_grade_trees + fifth_grade_trees + sixth_grade_trees
    result = total_trees_planted
    return result

print(solution())