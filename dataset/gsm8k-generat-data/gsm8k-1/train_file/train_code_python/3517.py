def solution():
    """Martha needs to paint all four walls in her 12 foot by 16 foot kitchen, which has 10 foot high ceilings. Each wall needs one coat of primer and two coats of paint. If Martha can paint 40 square feet per hour, how many hours will it take her to paint the kitchen?"""
    wall_height = 10
    room_width = 12
    room_length = 16
    wall_area = wall_height * room_width
    room_perimeter = 2 * (room_width + room_length)
    paint_area = (wall_area * 4) + (wall_height * room_perimeter)
    primer_hours = paint_area / 40
    paint_hours = (2 * paint_area) / 40
    total_hours = primer_hours + paint_hours
    result = total_hours
    return result

print(solution())