def solution():
    # Define the amount of square feet painted on each day
    monday_paint = 30
    tuesday_paint = 2 * monday_paint
    wednesday_paint = 0.5 * monday_paint

    # Calculate the total amount of square feet painted
    total_paint = monday_paint + tuesday_paint + wednesday_paint
    result = total_paint
    return result

print(solution())