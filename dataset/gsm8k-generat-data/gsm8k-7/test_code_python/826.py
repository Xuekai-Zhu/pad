def solution():
    units_per_semester = 20
    cost_per_unit = 50
    num_semesters = 2

    # Calculate the total number of units James takes
    total_units = units_per_semester * num_semesters

    # Calculate the total cost of tuition for James
    total_cost = total_units * cost_per_unit
    result = total_cost
    return result

print(solution())