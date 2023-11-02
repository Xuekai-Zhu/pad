def solution():
    # Calculate the total number of apples delivered
    total_apples = 180 * 12
    # Subtract the number of rotten apples
    remaining_apples = total_apples - 160
    # Calculate the number of boxes of apples
    boxes_of_apples = remaining_apples // 20
    result = boxes_of_apples
    return result

print(solution())