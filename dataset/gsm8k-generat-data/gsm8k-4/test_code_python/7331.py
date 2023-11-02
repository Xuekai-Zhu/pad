def solution():
    """The big bottles of mango juice hold 30 ounces and cost 2700 pesetas each. The small bottles hold 6 ounces and cost 600 pesetas each. How many pesetas would be saved by buying a big bottle instead of smaller bottles for the same volume of juice?"""
    # Define the volume of juice needed
    juice_volume = 30

    # Calculate the cost of buying the equivalent volume of juice in small bottles
    small_bottle_volume = 6
    num_small_bottles = juice_volume / small_bottle_volume
    cost_small_bottles = num_small_bottles * 600

    # Calculate the cost of buying a big bottle
    cost_big_bottle = 2700

    # Calculate the difference in cost
    cost_difference = cost_small_bottles - cost_big_bottle

    # return the result
    result = cost_difference
    return result

print(solution())