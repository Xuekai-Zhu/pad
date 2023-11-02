def solution():
    
    total_leaves = 12 + 13
    brown_leaves = 0.2 * total_leaves
    green_leaves = 0.2 * total_leaves
    yellow_leaves = total_leaves - brown_leaves - green_leaves
    result = yellow_leaves
    return result

print(solution())