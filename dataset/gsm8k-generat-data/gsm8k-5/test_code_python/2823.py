def solution():
    total_boxes = 50 + 25  # Merry had 50 boxes on Saturday and 25 on Sunday
    apples_per_box = 10  # Merry had 10 apples in each box
    total_apples_sold = 720  # Merry sold a total of 720 apples on Saturday and Sunday

    # Calculate the total number of apples remaining
    total_apples_remaining = (total_boxes * apples_per_box) - total_apples_sold

    # Convert the remaining apples to boxes
    boxes_remaining = total_apples_remaining / apples_per_box
    result = boxes_remaining
    return result

print(solution())