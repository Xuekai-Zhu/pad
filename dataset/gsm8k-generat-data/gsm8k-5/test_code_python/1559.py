def solution():
    blue_pen_cost = 0.10  # cost of each blue pen
    red_pen_cost = 2 * blue_pen_cost  # cost of each red pen, twice as much as blue pen

    # Calculate total cost of blue pens
    blue_pen_total_cost = blue_pen_cost * 10  # Maci needs 10 blue pens

    # Calculate total cost of red pens
    red_pen_total_cost = red_pen_cost * 15  # Maci needs 15 red pens

    # Calculate total cost of all pens
    total_cost = blue_pen_total_cost + red_pen_total_cost
    result = total_cost
    return result

print(solution())