def solution():
    """A school bought 20 cartons of pencils at the start of school. Pencils come in cartons of 10 boxes and each box costs $2. The school also bought 10 cartons of markers. A carton has 5 boxes and costs $4. How much did the school spend in all?"""
    # Define the cost of a box of pencils and a box of markers
    pencil_box_cost = 2
    marker_box_cost = 4

    # Calculate the total cost of pencils
    pencil_carton_cost = pencil_box_cost * 10
    total_pencil_cost = pencil_carton_cost * 20

    # Calculate the total cost of markers
    marker_carton_cost = marker_box_cost * 5
    total_marker_cost = marker_carton_cost * 10

    # Calculate the total cost of all supplies
    total_cost = total_pencil_cost + total_marker_cost

    # Return the result
    result = total_cost
    return result

print(solution())