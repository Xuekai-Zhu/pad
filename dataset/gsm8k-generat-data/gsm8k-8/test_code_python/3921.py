def solution():
    # Calculate the total number of branches
    total_branches = 200 + 180 + 180 + 153

    # Calculate the total height of the trees
    total_height = 50 + 40 + 60 + 34

    # Calculate the average number of branches per foot
    average_branches_per_foot = total_branches / total_height
    result = average_branches_per_foot
    return result

print(solution())