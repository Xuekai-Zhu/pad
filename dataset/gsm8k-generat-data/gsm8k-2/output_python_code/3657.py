def solution():
    """Twenty people pre-bought plane tickets at a price of $155 per ticket. Thirty people bought their plane tickets at the gate and they each paid $200 for their ticket. How many more dollars did the people at the gate pay for their tickets than those passengers that pre-bought their tickets?"""
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