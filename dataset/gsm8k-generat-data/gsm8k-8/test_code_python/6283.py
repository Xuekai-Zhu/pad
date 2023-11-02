def solution():
    # Calculate the cost of the prom tickets
    ticket_cost = 100 * 2

    # Calculate the cost of dinner
    dinner_cost = 120

    # Calculate the tip on the dinner bill
    tip = 0.3 * dinner_cost

    # Calculate the total cost of the limo rental
    limo_cost = 80 * 6

    # Calculate the total cost of everything
    total_cost = ticket_cost + dinner_cost + tip + limo_cost
    result = total_cost
    return result

print(solution())