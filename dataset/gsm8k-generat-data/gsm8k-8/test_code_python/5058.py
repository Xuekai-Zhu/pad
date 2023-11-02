def solution():
    # Number of trees planted by the 4th graders
    fourth_graders = 30

    # Number of trees planted by the 5th graders (twice as many as the 4th graders)
    fifth_graders = 2 * fourth_graders

    # Number of trees planted by the 6th graders (30 fewer than thrice the number of trees planted by the 5th graders)
    sixth_graders = 3 * fifth_graders - 30

    # Total number of trees planted
    total_trees = fourth_graders + fifth_graders + sixth_graders

    result = total_trees
    return result

print(solution())