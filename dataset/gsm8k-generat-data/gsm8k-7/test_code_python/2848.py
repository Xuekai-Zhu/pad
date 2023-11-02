def solution():
    cost_per_gallon = 45
    coverage_per_gallon = 400
    total_area = 1600
    num_coats = 2

    # Calculate the total amount of paint needed in gallons
    total_paint_needed = (total_area * num_coats) / coverage_per_gallon

    # Calculate the total cost of paint
    total_cost = total_paint_needed * cost_per_gallon

    # Divide the total cost between Jason and Jeremy
    cost_per_person = total_cost / 2
    result = cost_per_person
    return result

print(solution())