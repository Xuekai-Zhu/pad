def solution():
    walls = 5
    square_meters = (2 * 3) * walls
    minutes_per_square_meter = 10
    minutes_to_paint = square_meters * minutes_per_square_meter
    hours_available = 10
    hours_to_paint = minutes_to_paint / 60
    spare_hours = hours_available - hours_to_paint
    result = spare_hours
    return result

print(solution())