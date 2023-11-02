def solution():
    cost_per_square_foot = 5
    square_feet_per_seat = 12
    desired_seats = 500
    total_square_feet = desired_seats * square_feet_per_seat
    total_land_cost = total_square_feet * cost_per_square_foot
    total_construction_cost = 2 * total_land_cost
    partner_contribution = 0.4 * (total_land_cost + total_construction_cost)
    tom_spend = total_land_cost + total_construction_cost - partner_contribution
    result = tom_spend
    
    return result

print(solution())