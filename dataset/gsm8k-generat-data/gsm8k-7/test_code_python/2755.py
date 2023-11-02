def solution():
    pen_price = 0.15
    pencil_price = 0.25

    num_pens = 40
    num_pencils = int(num_pens * 2 / 5 + num_pens)

    # Calculate the total cost of all pens
    total_pen_cost = num_pens * pen_price

    # Calculate the total cost of all pencils
    total_pencil_cost = num_pencils * pencil_price

    # Calculate the total cost of all items
    total_cost = total_pen_cost + total_pencil_cost
    result = total_cost
    return result

print(solution())