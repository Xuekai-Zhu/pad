def solution():
     total_branches = 10
     sub_branches = 40
     leaves_per_branch = 60
     total_leaves = total_branches * sub_branches * leaves_per_branch
     return total_leaves

print(solution())