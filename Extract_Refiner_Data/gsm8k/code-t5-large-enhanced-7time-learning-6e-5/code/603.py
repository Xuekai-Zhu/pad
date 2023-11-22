def solution():
    
    # Define the cost of the shampoo bottle and the number of washings
    shampoo_cost = 2400
    washings = 120

    # Calculate the cost per pump
    pump_cost = shampoo_cost / washings

    # Convert the cost to cents
    cost_per_pump = pump_cost * 100

    # Display the cost per pump in cents
    result = cost_per_pump
    return result

print(solution())