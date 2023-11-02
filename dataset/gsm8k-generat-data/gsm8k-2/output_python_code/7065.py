def solution():
    """A school bought 20 cartons of pencils at the start of school. Pencils come in cartons of 10 boxes and each box costs $2. The school also bought 10 cartons of markers. A carton has 5 boxes and costs $4. How much did the school spend in all?"""
    pencil_cartons = 20
    pencil_boxes_per_carton = 10
    pencil_box_price = 2
    marker_cartons = 10
    marker_boxes_per_carton = 5
    marker_carton_price = 4

    pencil_cost = pencil_cartons * pencil_boxes_per_carton * pencil_box_price
    marker_cost = marker_cartons * marker_boxes_per_carton * marker_carton_price
    total_cost = pencil_cost + marker_cost

    result = total_cost
    return result

print(solution())