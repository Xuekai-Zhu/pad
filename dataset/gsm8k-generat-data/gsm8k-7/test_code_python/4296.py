def solution():
    cubic_feet_of_water = 6.0
    gallons_per_cubic_foot = 7.5
    pounds_per_gallon = 8.0
    tablespoons_per_pound = 1.5
    cost_per_tablespoon = 0.5

    # Calculate the total weight of water in the tub in pounds
    total_water_weight = cubic_feet_of_water * gallons_per_cubic_foot * pounds_per_gallon

    # Calculate the total number of tablespoons of jello mix needed
    total_jello_mix = total_water_weight * tablespoons_per_pound

    # Calculate the total cost of the jello mix
    total_cost = total_jello_mix * cost_per_tablespoon
    result = total_cost
    return result

print(solution())