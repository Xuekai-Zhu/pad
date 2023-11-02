def solution():
    # Calculate the total number of apples delivered
    total_apples = 42 * 12

    # Subtract the number of rotten apples
    total_apples -= 4

    # Calculate the number of boxes needed
    boxes_needed = total_apples // 10

    result = boxes_needed
    return result

print(solution())