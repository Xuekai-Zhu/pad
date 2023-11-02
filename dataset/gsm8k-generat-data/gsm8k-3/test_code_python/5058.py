def solution():
    """A school does a yearly tree planting activity. This year, the 4th graders planted a total of 30 trees while 5th graders planted twice as many. The 6th graders planted 30 fewer than thrice the number of trees planted by the 5th graders. How many trees did they plant altogether?"""
    # Total trees planted by 4th graders
    trees_4th = 30

    # Total trees planted by 5th graders
    trees_5th = 2 * trees_4th

    # Total trees planted by 6th graders
    trees_6th = 3 * trees_5th - 30

    # Total trees planted
    total_trees = trees_4th + trees_5th + trees_6th

    # Display the total number of trees planted
    result = total_trees
    return result

print(solution())