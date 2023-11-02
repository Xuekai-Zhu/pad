def solution():
    num_pre_bought = 20
    pre_bought_price = 155

    num_at_gate = 30
    at_gate_price = 200

    # Calculate the total cost paid by the people who pre-bought their tickets
    total_pre_bought_cost = num_pre_bought * pre_bought_price

    # Calculate the total cost paid by the people who bought their tickets at the gate
    total_at_gate_cost = num_at_gate * at_gate_price

    # Calculate the difference in cost between the two groups
    cost_difference = total_at_gate_cost - total_pre_bought_cost
    result = cost_difference
    return result

print(solution())