def solution():
    """A school does a yearly tree planting activity. This year, the 4th graders planted a total of 30 trees while 5th graders planted twice as many. The 6th graders planted 30 fewer than thrice the number of trees planted by the 5th graders. How many trees did they plant altogether?"""
    fourth_graders = 30
    fifth_graders = fourth_graders * 2
    sixth_graders = (fifth_graders * 3) - 30
    total_trees = fourth_graders + fifth_graders + sixth_graders
    result = total_trees
    return result

print(solution())