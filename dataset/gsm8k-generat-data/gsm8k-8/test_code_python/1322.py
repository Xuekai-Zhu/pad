def solution():
    # Define the variables
    cost_per_square_foot = 5
    space_per_seat = 12
    num_seats = 500
    construction_ratio = 2
    partner_coverage_ratio = 0.4

    # Calculate the total space needed
    total_space = num_seats * space_per_seat

    # Calculate the total cost for both land and construction
    total_cost = (total_space * cost_per_square_foot) * construction_ratio
    total_cost *= (1 + partner_coverage_ratio)

    result = total_cost
    return result

print(solution())