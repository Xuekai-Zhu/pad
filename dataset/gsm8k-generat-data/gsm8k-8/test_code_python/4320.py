def solution():
    # Calculate the area of the mural
    area = 6 * 3

    # Calculate the cost of the paint
    paint_cost = area * 4

    # Calculate the time it takes to paint the mural
    time = area / 1.5

    # Calculate the cost of labor
    labor_cost = time * 10

    # Calculate the total cost of the mural
    total_cost = paint_cost + labor_cost
    result = total_cost
    return result

print(solution())