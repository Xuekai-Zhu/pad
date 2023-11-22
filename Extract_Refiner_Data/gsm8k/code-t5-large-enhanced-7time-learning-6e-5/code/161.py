def solution():
    
    # Define the budget and the cost of each item
    budget = 1500
    machine_cost = 1090
    scanner_cost = 157
    CD_burner_cost = 74
    printer_cost = 102

    # Calculate the total cost of the garment
    total_cost = budget + machine_cost + scanner_cost + CD_burner_cost + printer_cost

    # Calculate the amount of money left over after paying for the garment
    money_left_over = total_cost - budget

    # return the result
    result = money_left_over
    return result

print(solution())