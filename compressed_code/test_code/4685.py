def solution():
    
    branches_per_tree = 10
    subbranches_per_branch = 40
    leaves_per_subbranch = 60
    leaves_per_branch = subbranches_per_branch * leaves_per_subbranch
    leaves_per_tree = branches_per_tree * leaves_per_branch
    total_leaves = leaves_per_tree * 4
    result = total_leaves
    return result

print(solution())