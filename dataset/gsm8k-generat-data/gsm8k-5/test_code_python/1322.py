def solution():
    cost_per_square_foot = 5  # The cost is $5 per square foot of space
    square_feet_per_seat = 12  # Tom needs 12 square feet of space for each seat
    num_seats = 500  # Tom wants a 500 seat theater
    total_square_feet = square_feet_per_seat * num_seats  # Calculate the total square feet needed for the theater
    total_cost = cost_per_square_foot * total_square_feet  # Calculate the cost of the land

    construction_cost = 2 * total_cost  # Construction will cost twice as much as the land
    total_cost += construction_cost  # Add the construction cost to the total cost

    partner_coverage = 0.4  # Tom's partner covers 40% of the cost
    tom_spends = total_cost * (1 - partner_coverage)  # Tom pays the remaining cost

    result = tom_spends
    return result

print(solution())