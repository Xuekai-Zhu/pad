def solution():
    # Calculate the number of times Felix got his axe sharpened
    sharpened_count = 35 // 5  # each axe sharpening costs $5
    # Calculate the minimum number of trees Felix chopped down
    tree_count = sharpened_count * 13
    result = tree_count
    return result

print(solution())