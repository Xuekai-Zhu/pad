def solution():
    # Calculate the total number of Oak Leaves collected
    total_leaves = 12 + 13

    # Calculate the number of Brown and Green leaves
    brown_green_leaves = total_leaves * 0.2

    # Calculate the number of Yellow leaves
    yellow_leaves = total_leaves - brown_green_leaves

    result = yellow_leaves
    return result

print(solution())