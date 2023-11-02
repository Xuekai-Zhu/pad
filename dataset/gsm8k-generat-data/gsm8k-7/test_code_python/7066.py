def solution():
    num_pencil_cartons = 20
    num_pencil_boxes_per_carton = 10
    pencil_box_cost = 2

    num_marker_cartons = 10
    num_marker_boxes_per_carton = 5
    marker_carton_cost = 4

    # Calculate the total cost of all pencil boxes
    total_pencil_boxes = num_pencil_cartons * num_pencil_boxes_per_carton
    total_pencil_cost = total_pencil_boxes * pencil_box_cost

    # Calculate the total cost of all marker cartons
    total_marker_cost = num_marker_cartons * marker_carton_cost

    # Calculate the total cost of all school supplies
    total_cost = total_pencil_cost + total_marker_cost
    result = total_cost
    return result

print(solution())