def solution():
    
    initial_leaves = 18
    remaining_leaves = initial_leaves - (initial_leaves / 3)
    total_leaves = remaining_leaves * 3
    result = total_leaves
    return result

print(solution())