def solution():
    # Calculate the cost of the canvas
    brush_cost = 20
    canvas_cost = 3 * brush_cost

    # Calculate the total cost of the tools and materials
    total_cost = brush_cost + canvas_cost + 8 * 5

    # Calculate Maria's earnings
    earnings = 200 - total_cost
    result = earnings
    return result

print(solution())