def solution():
    # Calculate the cost of the mixed set of paints
    paint_set_cost = (1/2) * 40 

    # Calculate the total cost of canvases and paint set
    canvas_paint_cost = 4 * 40 + paint_set_cost 

    # Calculate the remaining amount of money after buying canvases, paint set, and easel
    remaining_money = 90 - canvas_paint_cost - 15 

    result = remaining_money
    return result

print(solution())