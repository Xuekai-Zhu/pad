def solution():
    """A school does a yearly tree planting activity. This year, the 4th graders planted a total of 30 trees while 5th graders planted twice as many. The 6th graders planted 30 fewer than thrice the number of trees planted by the 5th graders. How many trees did they plant altogether?"""
    # Determine the number of trees planted by the 4th graders
    fourth_graders_trees = 30

    # Determine the number of trees planted by the 5th graders
    fifth_graders_trees = 2 * fourth_graders_trees

    # Determine the number of trees planted by the 6th graders
    sixth_graders_trees = 3 * fifth_graders_trees - 30

    # Determine the total number of trees planted
    total_trees_planted = fourth_graders_trees + fifth_graders_trees + sixth_graders_trees

    # return the result
    result = total_trees_planted
    return result

print(solution())