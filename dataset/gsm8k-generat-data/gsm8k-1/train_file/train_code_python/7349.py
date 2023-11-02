def solution():
    """Tonya spent $90.00 on art supplies. 4 canvases cost $40.00 and a mixed set of paints cost 1/2 that much. She also spent $15.00 on an easel, and the rest of the money on paintbrushes. How much money did she spend on paintbrushes?"""
    total_cost = 90
    canvas_cost = 40
    paint_set_cost = canvas_cost / 2
    easel_cost = 15
    paintbrush_cost = total_cost - canvas_cost - paint_set_cost - easel_cost
    result = paintbrush_cost
    return result

print(solution())