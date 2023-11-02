def solution():
    flower_cost = 9  # Cost of flowers
    pot_cost = flower_cost + 20  # Cost of clay pot is $20 more than the flowers
    soil_cost = flower_cost - 2  # Cost of bag of soil is $2 less than the flowers

    # Total cost of planting the flowers
    total_cost = flower_cost + pot_cost + soil_cost
    result = total_cost
    return result

print(solution())