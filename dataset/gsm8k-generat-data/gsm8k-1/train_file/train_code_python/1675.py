def solution():
    """Mikaela was repainting her bathroom. She bought 16 containers of paint to cover the four equally-sized walls. At the last minute, she decided to put tile on one wall in the bathroom and paint flowers on the ceiling with one container of paint instead. How many containers of paint will she have left over?"""
    initial_paint_containers = 16
    paint_used_for_ceiling = 1
    paint_used_for_tile = initial_paint_containers / 4
    paint_remaining = initial_paint_containers - paint_used_for_ceiling - paint_used_for_tile
    result = paint_remaining
    return result

print(solution())