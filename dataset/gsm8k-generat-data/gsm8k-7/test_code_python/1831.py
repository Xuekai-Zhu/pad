def solution():
    num_boxes = 15
    num_pencils_per_box = 80
    pencil_price = 4
    pen_price = 5

    # Calculate the total number of pencils ordered
    total_pencils = num_boxes * num_pencils_per_box

    # Calculate the number of pens ordered
    num_pens = 300 + (2 * total_pencils)

    # Calculate the total cost of all pencils
    total_pencil_cost = total_pencils * pencil_price

    # Calculate the total cost of all pens
    total_pen_cost = num_pens * pen_price

    # Calculate the total cost of all stationery
    total_cost = total_pencil_cost + total_pen_cost
    result = total_cost
    return result

print(solution())