def solution():
    
    pre_bought_tickets = 20
    gate_tickets = 30
    pre_bought_price = 155
    gate_price = 200
    pre_bought_total = pre_bought_tickets * pre_bought_price
    gate_total = gate_tickets * gate_price
    difference = gate_total - pre_bought_total
    result = difference
    
    return result

print(solution())