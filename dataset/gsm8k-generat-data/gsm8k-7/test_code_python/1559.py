def solution():
    num_blue_pens = 10
    blue_pen_price = 0.1

    num_red_pens = 15
    red_pen_price = 2 * blue_pen_price

    # Calculate the total cost of all blue pens
    total_blue_pen_cost = num_blue_pens * blue_pen_price

    # Calculate the total cost of all red pens
    total_red_pen_cost = num_red_pens * red_pen_price

    # Calculate the total cost of all pens
    total_cost = total_blue_pen_cost + total_red_pen_cost
    result = total_cost
    return result

print(solution())