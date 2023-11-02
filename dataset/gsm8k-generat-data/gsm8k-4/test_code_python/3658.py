def solution():
    """Twenty people pre-bought plane tickets at a price of $155 per ticket. Thirty people bought their plane tickets at the gate and they each paid $200 for their ticket. How many more dollars did the people at the gate pay for their tickets than those passengers that pre-bought their tickets?"""
    # Define the number of pre-bought tickets and their cost
    pre_bought_num = 20
    pre_bought_cost = 155

    # Define the number of gate tickets and their cost
    gate_num = 30
    gate_cost = 200

    # Calculate the total amount paid by pre-bought ticket holders
    pre_bought_total = pre_bought_num * pre_bought_cost

    # Calculate the total amount paid by gate ticket holders
    gate_total = gate_num * gate_cost

    # Calculate the difference in amount paid between gate and pre-bought tickets
    difference = gate_total - pre_bought_total

    # return the result
    result = difference
    return result

print(solution())