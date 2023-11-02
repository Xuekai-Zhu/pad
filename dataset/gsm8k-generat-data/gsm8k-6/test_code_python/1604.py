def solution():
    mary_paint = 3  # square feet of paint used by Mary
    mike_paint = mary_paint + 2  # square feet of paint used by Mike
    total_paint_used = mary_paint + mike_paint  # total square feet of paint used for dragon and castle
    paint_left = 13 - total_paint_used  # square feet of paint left in the jar
    result = paint_left
    return result

print(solution())