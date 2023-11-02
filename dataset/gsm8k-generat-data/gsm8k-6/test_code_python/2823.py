def solution():
    # Calculate the total number of apples that Merry had
    total_apples = (50 + 25) * 10  # 50 boxes on Saturday, 25 boxes on Sunday, 10 apples in each box

    # Calculate the boxes of apples remaining after selling 720 apples
    remaining_apples = total_apples - 720
    remaining_boxes = remaining_apples // 10
    result = remaining_boxes
    return result

print(solution())