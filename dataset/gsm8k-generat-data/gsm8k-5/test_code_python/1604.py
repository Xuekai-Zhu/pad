def solution():
    mary_paint = 3  # Mary used 3 square feet worth of paint
    mike_paint = mary_paint + 2  # Mike used 2 square feet more paint than Mary
    total_paint_used = mary_paint + mike_paint  # Total amount of paint used so far
    paint_left = 13 - total_paint_used  # Paint left for the sun

    # Calculate the area of the biggest sun possible
    area_of_sun = paint_left // 2  # Each square foot of paint covers 2 square feet area

    result = area_of_sun
    return result

print(solution())