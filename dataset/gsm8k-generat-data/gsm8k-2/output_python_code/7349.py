def solution():
    """Tonya spent $90.00 on art supplies. 4 canvases cost $40.00 and a mixed set of paints cost 1/2 that much. She also spent $15.00 on an easel, and the rest of the money on paintbrushes. How much money did she spend on paintbrushes?"""
    canvas_price = 40
    paint_price = 0.5 * canvas_price
    easel_price = 15
    total_spent = 90
    total_spent -= easel_price  # subtract easel price
    total_spent -= canvas_price  # subtract cost of 4 canvases
    total_spent -= paint_price  # subtract cost of paint
    result = total_spent
    return result

print(solution())