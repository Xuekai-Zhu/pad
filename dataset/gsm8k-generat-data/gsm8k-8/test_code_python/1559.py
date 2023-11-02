def solution():
    # Define the number of pens and their respective costs
    blue_pens = 10
    blue_pen_cost = 0.1
    red_pens = 15
    red_pen_cost = blue_pen_cost * 2

    # Calculate the total cost of the pens
    total_cost = (blue_pens * blue_pen_cost) + (red_pens * red_pen_cost)
    result = total_cost
    return result

print(solution())