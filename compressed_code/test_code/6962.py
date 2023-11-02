def solution():
    
    smoky_salmon_cost = 40
    black_burger_cost = 15
    chicken_katsu_cost = 25
    subtotal = smoky_salmon_cost + black_burger_cost + chicken_katsu_cost
    service_charge_percent = 10
    tip_percent = 5
    service_charge = subtotal * (service_charge_percent / 100)
    tip = subtotal * (tip_percent / 100)
    total_cost = subtotal + service_charge + tip
    change = 100 - total_cost
    result = change
    return result

print(solution())