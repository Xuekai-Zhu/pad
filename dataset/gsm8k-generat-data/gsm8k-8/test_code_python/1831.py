def solution():
    # Calculate the total number of pencils ordered
    total_pencils = 15 * 80

    # Calculate the total number of pens ordered
    total_pens = 2 * total_pencils + 300

    # Calculate the total cost of the pencils
    pencil_cost = total_pencils * 4

    # Calculate the total cost of the pens
    pen_cost = total_pens * 5

    # Calculate the total cost of the stationery
    total_cost = pencil_cost + pen_cost

    result = total_cost
    return result

print(solution())