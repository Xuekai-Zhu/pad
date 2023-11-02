def solution():
    apples = 10000
    apples_per_box = 50
    box_price = 35
    boxes_sold = apples / apples_per_box
    total_price = boxes_sold * box_price
    result = total_price
    return result

print(solution())