def solution():
    """Katerina purchases 3 pots and 4 pans at the home goods store. Each pot costs $20. The total cost of Katerina's items is $100. If each pan is the same price, what is the cost of 2 pans?"""
    pot_cost = 20
    total_cost = 100
    num_pots = 3
    num_pans = 4
    # calculate total cost of pots
    pot_total = pot_cost * num_pots
    # calculate total cost of pans
    pan_total = total_cost - pot_total
    # divide by number of pans to get cost per pan
    pan_cost = pan_total / num_pans
    # multiply by 2 to get cost of 2 pans
    result = pan_cost * 2
    return result

print(solution())