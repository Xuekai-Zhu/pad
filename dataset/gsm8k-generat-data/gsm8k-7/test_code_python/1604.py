def solution():
    mary_paint = 3
    mike_paint = mary_paint + 2
    total_paint_used = mary_paint + mike_paint

    # Calculate remaining paint after Mary and Mike painted their individual paintings
    remaining_paint = 13 - total_paint_used

    # Calculate the largest possible sun that Mary and Mike can paint with the remaining paint
    sun_paint = remaining_paint

    result = sun_paint
    return result

print(solution())