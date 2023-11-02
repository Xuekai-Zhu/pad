def solution():
    wall_area = 1600  # Total area of the walls they want to paint
    paint_coverage = 400  # Coverage of one gallon of paint in square feet
    num_gallons = (wall_area * 2) / paint_coverage  # They need two coats of paint, so double the area to be covered
    cost_per_gallon = 45  # Cost of one gallon of paint
    total_cost = num_gallons * cost_per_gallon  # Total cost of the paint

    # Split the cost equally between Jason and Jeremy
    cost_per_person = total_cost / 2
    result = cost_per_person
    return result

print(solution())