def solution():
    # Calculate the total weight of water in the bathtub in pounds
    water_volume_cubic_feet = 6
    water_volume_gallons = water_volume_cubic_feet * 7.5
    water_weight = water_volume_gallons * 8

    # Calculate the amount of jello mix needed in tablespoons
    jello_mix_ratio = 1.5 # tablespoons of jello mix per pound of water
    jello_mix_needed = jello_mix_ratio * water_weight

    # Calculate the cost of the jello mix needed
    jello_mix_cost_per_tablespoon = 0.5
    total_jello_mix_cost = jello_mix_needed * jello_mix_cost_per_tablespoon

    result = total_jello_mix_cost
    return result

print(solution())