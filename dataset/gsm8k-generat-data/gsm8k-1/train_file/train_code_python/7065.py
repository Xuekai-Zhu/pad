def solution():
    """A school bought 20 cartons of pencils at the start of school. Pencils come in cartons of 10 boxes and each box costs $2. The school also bought 10 cartons of markers. A carton has 5 boxes and costs $4. How much did the school spend in all?"""
    pencil_cartons = 20
    pencil_boxes_per_carton = 10
    pencil_box_cost = 2
    marker_cartons = 10
    marker_boxes_per_carton = 5
    marker_carton_cost = 4
    
    total_pencil_boxes = pencil_cartons * pencil_boxes_per_carton
    pencil_cost = total_pencil_boxes * pencil_box_cost
    
    total_marker_boxes = marker_cartons * marker_boxes_per_carton
    marker_cost = total_marker_boxes * marker_carton_cost
    
    total_cost = pencil_cost + marker_cost
    result = total_cost
    
    return result

print(solution())