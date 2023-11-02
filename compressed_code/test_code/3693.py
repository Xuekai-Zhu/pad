def solution():
    
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