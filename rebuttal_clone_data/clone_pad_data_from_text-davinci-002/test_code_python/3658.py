def solution():
     pre_bought_tickets = 20
     gate_tickets = 30
     price_pre_bought_tickets = 155
     price_gate_tickets = 200
     total_price_pre_bought_tickets = pre_bought_tickets * price_pre_bought_tickets
     total_price_gate_tickets = gate_tickets * price_gate_tickets
     difference = total_price_gate_tickets - total_price_pre_bought_tickets
     result = difference
     return result

print(solution())