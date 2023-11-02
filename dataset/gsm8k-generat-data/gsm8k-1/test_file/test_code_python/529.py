def solution():
    """Errol bought a computer, 2 monitors, and a printer for $2,400. He paid $400 less for the printer than the computer. If the computer cost $1,100, how much did one monitor cost, in dollars?"""
    total_cost = 2400
    computer_cost = 1100
    printer_cost = computer_cost - 400
    monitor_cost = (total_cost - computer_cost - printer_cost) / 2
    result = monitor_cost
    
    return result

print(solution())