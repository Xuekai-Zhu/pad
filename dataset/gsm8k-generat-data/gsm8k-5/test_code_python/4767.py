def solution():
    pot_cost = 20  # Each pot costs $20
    total_cost = 100  # The total cost of Katerina's items is $100
    pots = 3  # Katerina purchases 3 pots
    pans = 4  # Katerina purchases 4 pans

    # Calculate the cost of each pan
    pan_cost = (total_cost - (pot_cost * pots)) / pans

    # Calculate the cost of 2 pans
    cost_of_2_pans = pan_cost * 2
    result = cost_of_2_pans
    return result

print(solution())