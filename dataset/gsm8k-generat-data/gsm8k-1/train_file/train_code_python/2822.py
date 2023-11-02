def solution():
    """Merry had 50 boxes of apples on Saturday and 25 boxes on Sunday. There were 10 apples in each box. If she sold a total of 720 apples on Saturday and Sunday, how many boxes of apples are left?"""
    total_boxes = 50 + 25
    apples_sold = 720
    apples_per_box = 10
    total_apples = total_boxes * apples_per_box
    apples_left = total_apples - apples_sold
    boxes_left = apples_left / apples_per_box
    result = boxes_left
    return result

print(solution())