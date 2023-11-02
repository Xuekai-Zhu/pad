def solution():
    
    # Define the cost of the jumbo bottle and the number of pumps needed
    BOTTLE_COST = 24.00
    NUM_PUMPS = 120

    # Calculate the number of washings needed
    num_washings = NUM_PUMPS * 2

    # Calculate the cost per pump
    cost_per_pump = BOTTLE_COST / num_washings

    # Convert the cost per pump to cents
    cost_per_pump_cents = cost_per_pump * 100

    # Display the cost per pump in cents
    result = cost_per_pump_cents
    return result

print(solution())