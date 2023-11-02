def solution():
    """James decides to make a bathtub full of jello.  For every pound of water, you need 1.5 tablespoons of jello mix.  The bathtub can hold 6 cubic feet of water.  Each cubic foot of water is 7.5 gallons.  A gallon of water weighs 8 pounds.  A tablespoon of jello mix costs $0.50.  How much did he spend to fill his tub?"""
    # Define the amount of jello mix needed per pound of water
    JELLO_MIX_PER_POUND_OF_WATER = 1.5

    # Calculate the amount of water the bathtub can hold in pounds
    water_in_gallons = 6 * 7.5
    water_in_pounds = water_in_gallons * 8

    # Calculate the amount of jello mix needed in tablespoons
    jello_mix_in_tablespoons = water_in_pounds * JELLO_MIX_PER_POUND_OF_WATER

    # Calculate the cost of the jello mix
    jello_mix_cost = jello_mix_in_tablespoons * 0.5

    # Display the total cost of the jello mix
    result = jello_mix_cost
    return result

print(solution())