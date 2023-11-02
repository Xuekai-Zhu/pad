def solution():
    # Calculate the total cost of canvases and mixed set of paints
    total_canvases_cost = 40.00 # 4 canvases cost $40.00
    mixed_paints_cost = total_canvases_cost / 2 # A mixed set of paints cost 1/2 that much
    total_canvas_paint_cost = total_canvases_cost + mixed_paints_cost 

    # Calculate the total cost of all items except paintbrushes
    total_other_cost = total_canvas_paint_cost + 15.00 # $15.00 on an easel

    # Calculate the cost of paintbrushes
    total_cost = 90.00 # $90.00 on art supplies
    paintbrushes_cost = total_cost - total_other_cost

    result = paintbrushes_cost
    return result

print(solution())