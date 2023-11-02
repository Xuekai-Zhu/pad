def solution():
    """The big bottles of mango juice hold 30 ounces and cost 2700 pesetas each. The small bottles hold 6 ounces and cost 600 pesetas each. How many pesetas would be saved by buying a big bottle instead of smaller bottles for the same volume of juice?"""
    # Define the volume of juice needed
    volume = 30

    # Calculate the cost of buying small bottles to get the same volume of juice
    num_small_bottles = volume / 6
    small_bottle_cost = num_small_bottles * 600

    # Calculate the cost of buying one big bottle
    big_bottle_cost = 2700

    # Calculate the pesetas saved by buying a big bottle
    pesetas_saved = small_bottle_cost - big_bottle_cost

    # Display the pesetas saved
    result = pesetas_saved
    return result

print(solution())