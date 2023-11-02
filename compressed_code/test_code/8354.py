def solution():
    
    branches = 30
    twigs_per_branch = 90
    total_twigs = branches * twigs_per_branch
    sprout_4_leaves = total_twigs * 0.3
    sprout_5_leaves = total_twigs - sprout_4_leaves
    total_leaves = (sprout_4_leaves * 4) + (sprout_5_leaves * 5)
    result = total_leaves
    return result

print(solution())