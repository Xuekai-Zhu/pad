def solution():
    previous_quantity = 10  # Chester previously delivered 10 bales of hay
    new_quantity = previous_quantity * 2  # Chester now has to deliver double the amount of hay
    previous_price = 15  # The previous hay cost $15 per bale
    new_price = 18  # The better quality hay costs $18 per bale

    # Calculate the cost of previous hay and new hay
    previous_cost = previous_quantity * previous_price
    new_cost = new_quantity * new_price

    # Calculate the difference in cost
    cost_difference = new_cost - previous_cost
    result = cost_difference
    return result

print(solution())