def solution():
    
    num_blue_pens = 10
    num_red_pens = 15
    cost_blue_pen = 0.1
    cost_red_pen = 2 * cost_blue_pen
    total_cost = (num_blue_pens * cost_blue_pen) + (num_red_pens * cost_red_pen)
    result = total_cost
    return result

print(solution())