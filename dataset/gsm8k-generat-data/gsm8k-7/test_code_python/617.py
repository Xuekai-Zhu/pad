def solution():
    base_fine = 50
    speed_limit = 30
    speed_over_limit = 75 - speed_limit
    additional_fine = speed_over_limit * 2
    fine_in_school_zone = additional_fine * 2
    court_costs = 300
    lawyer_cost = 80 * 3

    # Calculate the total fine
    total_fine = base_fine + fine_in_school_zone + court_costs + lawyer_cost
    result = total_fine
    return result

print(solution())