def solution():
    # Calculate the total weight of water in the bathtub
    total_gallons = 6 * 7.5  # 6 cubic feet of water, each cubic foot contains 7.5 gallons
    total_weight = total_gallons * 8  # Each gallon of water weighs 8 pounds

    # Calculate the amount of jello mix needed for the bathtub
    jello_mix_per_pound = 1.5  # 1.5 tablespoons of jello mix per pound of water
    jello_mix_needed = total_weight * jello_mix_per_pound

    # Calculate the cost of the jello mix
    cost_per_tablespoon = 0.5  # $0.50 per tablespoon of jello mix
    total_cost = jello_mix_needed * cost_per_tablespoon
    result = total_cost
    return result

print(solution())