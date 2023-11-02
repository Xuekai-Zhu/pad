def solution():
    # Calculate the total amount of water in the bathtub
    water_volume = 6 * 7.5  # each cubic foot of water is 7.5 gallons, and the bathtub can hold 6 cubic feet of water
    water_weight = water_volume * 8  # a gallon of water weighs 8 pounds, so multiply by 8 to get the weight of the water in pounds
    jello_mix = water_weight * 1.5 / 16  # for every 1 pound of water, 1.5 tablespoons of jello mix is needed. 16 tablespoons are in a pound.
    cost = jello_mix * 0.50  # each tablespoon of jello mix costs $0.50
    result = cost
    return result

print(solution())