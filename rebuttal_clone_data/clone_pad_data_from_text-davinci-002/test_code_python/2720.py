def solution():
    total_boxes = 33
    sold_Aunt = 12
    sold_Mother = 5
    sold_Neighbor = 4
    boxes_left = total_boxes - (sold_Aunt + sold_Mother + sold_Neighbor)
    result = boxes_left
    return result

print(solution())