def solution():
    total_spent = 90.0
    canvas_cost = 40.0
    paint_set_cost = canvas_cost / 2
    easel_cost = 15.0

    # Calculate the total cost of canvases and paint set
    canvas_and_paint_cost = 4 * canvas_cost + paint_set_cost

    # Calculate the amount spent on paintbrushes
    paintbrush_cost = total_spent - canvas_and_paint_cost - easel_cost
    result = paintbrush_cost
    return result

print(solution())