def solution():
    # Calculate the total cost
    ticket_cost = 2 * 100  # James pays for two tickets at $100 each
    dinner_cost = 120
    tip_amount = 0.3 * dinner_cost
    limo_cost = 80 * 6
    total_cost = ticket_cost + dinner_cost + tip_amount + limo_cost
    result = total_cost
    return result

print(solution())