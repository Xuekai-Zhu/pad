def solution():
    
    pot_cost = 20
    total_cost = 100
    num_pots = 3
    num_pans = 4
    
    pot_total = pot_cost * num_pots
    
    pan_total = total_cost - pot_total
    
    pan_cost = pan_total / num_pans
    
    result = pan_cost * 2
    return result

print(solution())