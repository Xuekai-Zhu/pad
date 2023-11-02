def solution():
    """Tonya spent $90.00 on art supplies.  4 canvases cost $40.00 and a mixed set of paints cost 1/2 that much. She also spent $15.00 on an easel, and the rest of the money on paintbrushes. How much money did she spend on paintbrushes?"""
    
    # Calculate the cost of the canvases
    canvas_cost = 40

    # Calculate the cost of the mixed set of paints
    paint_cost = canvas_cost / 2

    # Calculate the total cost of canvases and paints
    canvas_paint_cost = canvas_cost + paint_cost

    # Calculate the remaining amount Tonya spent on the easel and paintbrushes
    remaining_cost = 90 - canvas_paint_cost - 15

    # The remaining amount is what Tonya spent on paintbrushes
    result = remaining_cost
    return result

print(solution())