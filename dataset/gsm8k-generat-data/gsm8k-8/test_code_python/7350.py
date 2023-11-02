def solution():
    # Calculate the cost of the paints and the canvases
    canvas_cost = 40
    paint_cost = canvas_cost / 2
    total_art_cost = 4 * canvas_cost + paint_cost

    # Calculate the total cost of the art supplies
    total_cost = total_art_cost + 15

    # Calculate the cost of the paintbrushes
    paintbrush_cost = 90 - total_cost
    result = paintbrush_cost
    return result

print(solution())