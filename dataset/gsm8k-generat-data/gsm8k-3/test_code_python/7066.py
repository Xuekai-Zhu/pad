def solution():
    """A school bought 20 cartons of pencils at the start of school. Pencils come in cartons of 10 boxes and each box costs $2. The school also bought 10 cartons of markers. A carton has 5 boxes and costs $4. How much did the school spend in all?"""
    # Define the cost of each item
    PENCIL_BOX_PRICE = 2
    MARKER_BOX_PRICE = 4

    # Define the number of each item purchased
    pencil_cartons = 20
    marker_cartons = 10

    # Calculate the total cost of the pencils
    pencil_cost = pencil_cartons * 10 * PENCIL_BOX_PRICE

    # Calculate the total cost of the markers
    marker_cost = marker_cartons * 5 * MARKER_BOX_PRICE

    # Calculate the total cost of all the items
    total_cost = pencil_cost + marker_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())