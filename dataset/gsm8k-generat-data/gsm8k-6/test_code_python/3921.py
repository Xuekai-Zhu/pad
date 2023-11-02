def solution():
    # Calculate the total number of branches and height of all the trees
    total_branches = 200 + 180 + 180 + 153  # the sum of the branches of all 4 trees
    total_height = 50 + 40 + 60 + 34  # the sum of the height of all 4 trees

    # Calculate the average number of branches per foot
    branches_per_foot = total_branches / total_height
    result = branches_per_foot
    return result

print(solution())