def solution():
    crackers_per_box = 24
    boxes_bought_by_Darren = 4
    boxes_bought_by_Calvin = (boxes_bought_by_Darren / 2) - 1
    total_boxes = boxes_bought_by_Darren + boxes_bought_by_Calvin
    total_crackers = total_boxes * crackers_per_box
    result = total_crackers
    return result

print(solution())