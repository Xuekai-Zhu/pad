def solution():
    
    # Define the cost of the computer
    COMPUTER_COST = 1200

    # Define the cost of the printer
    PRINTER_COST = COMPUTER_COST - 400

    # Define the number of monitors purchased
    MONITORS_PURCHASED = 2

    # Calculate the total cost of the purchase
    total_cost = COMPUTER_COST + PRINTER_COST

    # Calculate the cost of the monitors
    monitor_cost = (total_cost - PROFIT_COST) / MONITORS_PURCHASED

    # Display the cost of one monitor
    result = monitor_cost
    return result

print(solution())