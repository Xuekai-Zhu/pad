def solution():
    """Tonya spent $90.00 on art supplies.  4 canvases cost $40.00 and a mixed set of paints cost 1/2 that much. She also spent $15.00 on an easel, and the rest of the money on paintbrushes. How much money did she spend on paintbrushes?"""
    # Define the cost of canvases and paints
    CANVAS_COST = 40.00
    PAINT_COST = CANVAS_COST / 2.00

    # Calculate the cost of the canvases
    canvas_cost = 4 * CANVAS_COST

    # Calculate the cost of the paints
    paint_cost = PAINT_COST

    # Calculate the cost of the easel
    easel_cost = 15.00

    # Calculate the total cost of the canvases, paints, and easel
    total_cost = canvas_cost + paint_cost + easel_cost

    # Calculate the amount spent on paintbrushes
    paintbrushes_cost = 90.00 - total_cost

    # Display the amount spent on paintbrushes
    result = paintbrushes_cost
    return result

print(solution())