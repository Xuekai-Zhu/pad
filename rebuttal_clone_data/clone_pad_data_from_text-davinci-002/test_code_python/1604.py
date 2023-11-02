def solution():
    paint_for_dragon = 3
    paint_for_castle = paint_for_dragon + 2
    total_paint = paint_for_dragon + paint_for_castle
    paint_left = 13 - total_paint
    result = paint_left
    return result

print(solution())