def solution():
    boxes_sold_Saturday = 60
    boxes_sold_Sunday = boxes_sold_Saturday + (boxes_sold_Saturday / 2)
    total_boxes_sold = boxes_sold_Saturday + boxes_sold_Sunday
    result = total_boxes_sold
    
    return result

print(solution())