def solution():
    pencil_cartons = 20
    pencil_boxes_per_carton = 10
    pencil_box_cost = 2
    total_pencil_cost = pencil_cartons * pencil_boxes_per_carton * pencil_box_cost
    
    marker_cartons = 10
    marker_boxes_per_carton = 5
    marker_box_cost = 4
    total_marker_cost = marker_cartons * marker_boxes_per_carton * marker_box_cost
    
    total_cost = total_pencil_cost + total_marker_cost
    
    result = total_cost
    
    return result

print(solution())