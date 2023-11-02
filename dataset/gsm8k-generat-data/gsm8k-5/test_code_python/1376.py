def solution():
    # Total number of leaves collected
    total_leaves = 12 + 13  # 12 leaves on Thursday, 13 on Friday

    # Number of brown leaves
    brown_leaves = round(total_leaves * 0.2)  # 20% of the leaves are brown

    # Number of green leaves
    green_leaves = round(total_leaves * 0.2)  # 20% of the leaves are green

    # Number of yellow leaves
    yellow_leaves = total_leaves - brown_leaves - green_leaves

    result = yellow_leaves
    return result

print(solution())