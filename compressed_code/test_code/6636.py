def solution():
    
    steak_cost = 20
    drink_cost = 5
    total_cost = (steak_cost * 2) + (drink_cost * 2)
    tip_percent = 20
    tip_amount = total_cost * (tip_percent / 100)
    billy_tip_amount = tip_amount * 0.8
    result = billy_tip_amount
    return result

print(solution())