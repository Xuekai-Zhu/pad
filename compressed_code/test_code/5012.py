def solution():
    
    num_boxes = 400
    box_cost = 80 + 165
    total_cost = num_boxes * box_cost
    donated_amount = total_cost * 4
    total_boxes = (donated_amount + total_cost) // box_cost
    result = total_boxes
    return result

print(solution())