def solution():
    """Jim decides to buy mayo in bulk. He can buy 1 gallon of mayo at Costco for 8 dollars. At the normal store, a 16-ounce bottle costs $3. How much money does he save by buying the gallon container?"""
    # Define the cost of a 16-ounce bottle of mayo
    bottle_cost = 3

    # Calculate the cost per ounce of mayo for the bottle
    bottle_cost_per_ounce = bottle_cost / 16

    # Calculate the cost per ounce of mayo for the gallon container
    gallon_cost_per_ounce = 8 / 128

    # Calculate the total cost for the same amount of mayo using the two options
    bottle_total_cost = 6 * bottle_cost_per_ounce
    gallon_total_cost = 128 * gallon_cost_per_ounce

    # Calculate the amount saved by purchasing the gallon container
    saved_amount = bottle_total_cost - gallon_total_cost

    # Return the result
    result = saved_amount
    return result

print(solution())