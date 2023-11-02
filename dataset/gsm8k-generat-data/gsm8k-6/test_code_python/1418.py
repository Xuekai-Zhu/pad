def solution():
    # Calculate the total cost of tools and materials
    brush_cost = 20
    canvas_cost = 3 * brush_cost
    paint_cost = 8 * 5

    total_cost = brush_cost + canvas_cost + paint_cost

    # Calculate Maria's profit if she sells the painting for $200
    profit = 200 - total_cost
    result = profit
    return result

print(solution())