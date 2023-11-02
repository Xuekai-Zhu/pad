def solution():
    """James decides to make a bathtub full of jello. For every pound of water, you need 1.5 tablespoons of jello mix. The bathtub can hold 6 cubic feet of water. Each cubic foot of water is 7.5 gallons. A gallon of water weighs 8 pounds. A tablespoon of jello mix costs $0.50. How much did he spend to fill his tub?"""
    # calculations for water
    cubic_feet = 6
    gallons = cubic_feet * 7.5
    pounds_of_water = gallons * 8

    # calculations for jello mix
    tablespoons_per_pound = 1.5
    tablespoons_needed = pounds_of_water * tablespoons_per_pound
    cost_per_tablespoon = 0.5
    total_cost = tablespoons_needed * cost_per_tablespoon

    result = total_cost
    return result

print(solution())