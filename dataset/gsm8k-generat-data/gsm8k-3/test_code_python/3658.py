def solution():
    """Twenty people pre-bought plane tickets at a price of $155 per ticket. Thirty people bought their plane tickets at the gate and they each paid $200 for their ticket. How many more dollars did the people at the gate pay for their tickets than those passengers that pre-bought their tickets?"""
    # Define the number of people who pre-bought plane tickets and the price per ticket
    pre_bought = 20
    pre_bought_price = 155

    # Define the number of people who bought tickets at the gate and the price per ticket
    gate_bought = 30
    gate_bought_price = 200

    # Calculate the total cost of pre-bought tickets
    pre_bought_cost = pre_bought * pre_bought_price

    # Calculate the total cost of tickets bought at the gate
    gate_bought_cost = gate_bought * gate_bought_price

    # Calculate the difference between the total cost of tickets bought at the gate and those pre-bought
    difference = gate_bought_cost - pre_bought_cost

    # Display the difference
    result = difference
    return result

print(solution())