def solution():
    num_pencils = 38
    pencil_cost = 2.5

    num_pens = 56
    pen_cost = 3.5

    # Calculate the total cost of all pencils
    total_pencil_cost = num_pencils * pencil_cost

    # Calculate the total cost of all pens
    total_pen_cost = num_pens * pen_cost

    # Calculate the total cost of all pencils and pens
    total_cost = total_pencil_cost + total_pen_cost
    result = total_cost
    return result

print(solution())