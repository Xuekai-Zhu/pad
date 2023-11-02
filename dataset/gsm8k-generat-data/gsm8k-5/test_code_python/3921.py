def solution():
    # Calculate total number of branches
    total_branches = 200 + 180 + 180 + 153

    # Calculate total height of trees
    total_height = 50 + 40 + 60 + 34

    # Calculate average number of branches per foot
    branches_per_foot = total_branches / total_height

    result = branches_per_foot
    return result

print(solution())