def solution():
    # Calculate the total cost of pencils
    cost_pencils = 20 * 10 * 2  # 20 cartons, 10 boxes per carton, $2 per box

    # Calculate the total cost of markers
    cost_markers = 10 * 5 * 4  # 10 cartons, 5 boxes per carton, $4 per box

    # Calculate the total amount spent by the school
    total_cost = cost_pencils + cost_markers
    result = total_cost
    return result

print(solution())