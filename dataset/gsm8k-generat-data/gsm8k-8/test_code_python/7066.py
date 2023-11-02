def solution():
    # Calculate the cost of pencils
    pencil_cartons = 20
    pencil_boxes = pencil_cartons * 10
    pencil_cost = pencil_boxes * 2

    # Calculate the cost of markers
    marker_cartons = 10
    marker_boxes = marker_cartons * 5
    marker_cost = marker_boxes * 4

    # Calculate the total cost
    total_cost = pencil_cost + marker_cost
    result = total_cost
    return result

print(solution())