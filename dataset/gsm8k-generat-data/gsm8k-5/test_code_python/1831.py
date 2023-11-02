def solution():
    # Calculate the total number of pencils ordered
    num_pencils = 15 * 80

    # Calculate the total number of pens ordered
    num_pens = 300 + 2 * num_pencils

    # Calculate the cost of pencils and pens
    cost_pencils = num_pencils * 4
    cost_pens = num_pens * 5

    # Calculate the total cost of stationery
    total_cost = cost_pencils + cost_pens
    result = total_cost
    return result

print(solution())