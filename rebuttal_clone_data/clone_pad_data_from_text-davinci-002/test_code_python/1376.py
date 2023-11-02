def solution():
     total_leaves = 12 + 13
     brown_leaves = total_leaves * 0.2
     green_leaves = total_leaves * 0.2
     yellow_leaves = total_leaves - (brown_leaves + green_leaves)
     result = yellow_leaves
     return result

print(solution())