def solution():
    mural_area = 6*3  # area of mural in square meters
    paint_cost = 4*mural_area  # total cost of paint
    time_taken = mural_area/1.5  # time taken to paint the mural in hours
    labor_cost = time_taken*10  # total cost of labor
    total_cost = paint_cost + labor_cost  # total cost of mural
    result = total_cost
    return result

print(solution())