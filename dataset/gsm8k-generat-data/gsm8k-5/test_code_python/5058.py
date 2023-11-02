def solution():
    fourth_graders = 30  # 30 trees were planted by the 4th graders
    fifth_graders = 2 * fourth_graders  # 5th graders planted twice as many as 4th graders
    sixth_graders = 3 * fifth_graders - 30  # 6th graders planted 30 fewer than thrice the number of trees planted by the 5th graders

    # Calculate the total number of trees planted by all the students
    total_trees = fourth_graders + fifth_graders + sixth_graders
    result = total_trees
    return result

print(solution())