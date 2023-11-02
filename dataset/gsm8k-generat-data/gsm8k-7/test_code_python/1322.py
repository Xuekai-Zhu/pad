def solution():
    cost_per_sf = 5.0
    sq_ft_per_seat = 12
    num_seats = 500
    construction_cost_multiplier = 2.0
    partner_coverage_percentage = 0.4

    # Calculate the total square footage needed for the theater
    total_sf = num_seats * sq_ft_per_seat

    # Calculate the total cost of the land
    land_cost = total_sf * cost_per_sf

    # Calculate the total cost of construction
    construction_cost = land_cost * construction_cost_multiplier

    # Calculate the total cost of the theater
    total_cost = land_cost + construction_cost

    # Calculate the amount covered by the partner
    partner_coverage = total_cost * partner_coverage_percentage

    # Calculate the amount spent by Tom
    tom_cost = total_cost - partner_coverage
    result = tom_cost
    return result

print(solution())