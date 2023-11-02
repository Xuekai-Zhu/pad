def solution():
    
    initial_leaves = 18
    fallen_leaves = initial_leaves / 3
    remaining_leaves = initial_leaves - fallen_leaves
    total_remaining_leaves = remaining_leaves * 3
    result = total_remaining_leaves
    return result

print(solution())