def solution():
    brush_cost = 20
    canvas_cost = brush_cost * 3
    paint_cost = 8

    # Calculate the total cost of all materials
    total_cost = brush_cost + canvas_cost + (paint_cost * 5)

    # Calculate Maria's profit from selling the painting
    profit = 200 - total_cost

    result = profit
    return result

print(solution())