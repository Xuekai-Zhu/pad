def solution():
    """James decides to make a bathtub full of jello. For every pound of water, you need 1.5 tablespoons of jello mix. The bathtub can hold 6 cubic feet of water. Each cubic foot of water is 7.5 gallons. A gallon of water weighs 8 pounds. A tablespoon of jello mix costs $0.50. How much did he spend to fill his tub?"""
    water_volume = 6 * 7.5  # 45 gallons
    water_weight = water_volume * 8  # 360 pounds
    jello_mix = 1.5 * water_weight  # 540 tablespoons
    jello_cost = jello_mix * 0.5  # cost of jello mix
    result = jello_cost
    return result

print(solution())