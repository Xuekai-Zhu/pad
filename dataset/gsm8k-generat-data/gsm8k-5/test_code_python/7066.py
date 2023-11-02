def solution():
    # Cost of pencils
    boxes_of_pencils = 20 * 10  # 20 cartons, each with 10 boxes
    cost_per_pencil_box = 2  # Each box of pencils costs $2
    total_cost_pencils = boxes_of_pencils * cost_per_pencil_box

    # Cost of markers
    boxes_of_markers = 10 * 5  # 10 cartons, each with 5 boxes
    cost_per_marker_box = 4  # Each box of markers costs $4
    total_cost_markers = boxes_of_markers * cost_per_marker_box

    # Total cost of pencils and markers
    total_cost = total_cost_pencils + total_cost_markers
    result = total_cost
    return result

print(solution())