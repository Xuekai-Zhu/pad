def solution():
    
    brush_cost = 20
    canvas_cost = 3 * brush_cost
    paint_cost = 8 * 5
    total_cost = brush_cost + canvas_cost + paint_cost
    selling_price = 200
    profit = selling_price - total_cost
    result = profit
    return result

print(solution())