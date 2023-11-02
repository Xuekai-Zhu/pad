def solution():
    """Katerina purchases 3 pots and 4 pans at the home goods store. Each pot costs $20. The total cost of Katerina's items is $100. If each pan is the same price, what is the cost of 2 pans?"""
    total_cost = 100
    pot_price = 20
    num_pots = 3
    num_pans = 4
    pans_total_price = total_cost - pot_price * num_pots
    pan_price = pans_total_price / num_pans
    cost_of_2_pans = pan_price * 2
    result = cost_of_2_pans
    return result

print(solution())