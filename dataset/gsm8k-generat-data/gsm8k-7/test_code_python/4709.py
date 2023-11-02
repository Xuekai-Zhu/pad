def solution():
    monday_paint = 30
    tuesday_paint = 2 * monday_paint
    wednesday_paint = monday_paint / 2

    total_paint = monday_paint + tuesday_paint + wednesday_paint
    result = total_paint
    return result

print(solution())