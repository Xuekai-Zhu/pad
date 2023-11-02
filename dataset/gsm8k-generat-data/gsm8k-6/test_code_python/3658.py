def solution():
    # Calculate the total cost of pre-bought tickets
    pre_bought_cost = 20 * 155  

    # Calculate the total cost of tickets bought at the gate
    gate_bought_cost = 30 * 200  

    # Calculate the difference in cost between the tickets bought at the gate and those bought pre-bought
    difference = gate_bought_cost - pre_bought_cost
    result = difference
    return result

print(solution())