def solution():
    
    meat_ravioli_weight = 1.5
    pumpkin_ravioli_weight = 1.25
    cheese_ravioli_weight = 1
    javier_meat = 5 * meat_ravioli_weight
    javier_pumpkin = 2 * pumpkin_ravioli_weight
    javier_cheese = 4 * cheese_ravioli_weight
    brother_pumpkin = 12 * pumpkin_ravioli_weight
    javier_total = javier_meat + javier_pumpkin + javier_cheese
    brother_total = brother_pumpkin
    result = max(javier_total, brother_total)
    return result

print(solution())