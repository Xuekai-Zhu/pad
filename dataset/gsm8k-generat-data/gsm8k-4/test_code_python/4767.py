def solution():
    """Katerina purchases 3 pots and 4 pans at the home goods store. Each pot costs $20. The total cost of Katerina's items is $100. If each pan is the same price, what is the cost of 2 pans?"""
    # Define the cost of each pot and the total cost of all pots
    pot_cost = 20
    total_pot_cost = 3 * pot_cost

    # Calculate the cost of all pans
    total_pan_cost = 100 - total_pot_cost

    # Divide the total pan cost by the number of pans to get the cost of each pan
    pan_cost = total_pan_cost / 4

    # Calculate the cost of 2 pans
    two_pan_cost = pan_cost * 2

    # return the result
    result = two_pan_cost
    return result

print(solution())