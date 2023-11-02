def solution():
    # Calculate the total gallons of paint needed for two coats
    total_area = 1600  # total area of their walls
    coverage_per_gallon = 400  # square feet of coverage per gallon of paint
    total_gallons = (total_area * 2) / coverage_per_gallon  # each wall needs two coats of paint

    # Calculate the total cost of the paint
    cost_per_gallon = 45  # cost of one gallon of paint
    total_cost = total_gallons * cost_per_gallon  # total cost of the paint

    # Calculate how much each person needs to contribute
    contribution_per_person = total_cost / 2  # they agreed to split the cost
    result = contribution_per_person
    return result

print(solution())