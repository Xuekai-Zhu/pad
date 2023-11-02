def solution():
    """James decides to make a bathtub full of jello. For every pound of water, you need 1.5 tablespoons of jello mix. The bathtub can hold 6 cubic feet of water. Each cubic foot of water is 7.5 gallons. A gallon of water weighs 8 pounds. A tablespoon of jello mix costs $0.50. How much did he spend to fill his tub?"""
    # Define the constants
    WATER_PER_CUBIC_FOOT = 7.5  # gallons
    POUNDS_PER_GALLON = 8.0
    JELLO_PER_POUND = 1.5  # tablespoons
    COST_PER_TABLESPOON = 0.5  # dollars

    # Define the variables
    jello_mix = 0.0  # tablespoons
    water_weight = 0.0  # pounds
    cost = 0.0  # dollars

    # Calculate the amount of water in the tub in pounds
    water_weight = WATER_PER_CUBIC_FOOT * 6.0 * POUNDS_PER_GALLON

    # Calculate the amount of jello mix needed in tablespoons
    jello_mix = water_weight * JELLO_PER_POUND

    # Calculate the cost of the jello mix
    cost = jello_mix * COST_PER_TABLESPOON

    # return the result
    result = cost
    return result

print(solution())