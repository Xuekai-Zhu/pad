def solution():
    # Calculate the total square feet of wall painted by Elisa in her house
    monday_paint = 30
    tuesday_paint = 2 * monday_paint
    wednesday_paint = 0.5 * monday_paint
    total_paint = monday_paint + tuesday_paint + wednesday_paint
    result = total_paint
    return result

print(solution())