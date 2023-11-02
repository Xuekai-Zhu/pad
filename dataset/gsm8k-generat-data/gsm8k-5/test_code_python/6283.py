def solution():
    num_tickets = 2  # James buys tickets for himself and Susan
    ticket_cost = 100  # Each ticket costs $100
    dinner_cost = 120
    tip_percent = 30  # James leaves a 30% tip
    limo_hours = 6
    limo_cost_per_hour = 80

    # Calculate the total cost of the tickets
    ticket_total = num_tickets * ticket_cost

    # Calculate the total cost of dinner with tip
    tip_amount = dinner_cost * (tip_percent / 100)
    dinner_total = dinner_cost + tip_amount

    # Calculate the total cost of the limo rental
    limo_total = limo_hours * limo_cost_per_hour

    # Calculate the overall total cost
    total_cost = ticket_total + dinner_total + limo_total
    result = total_cost
    return result

print(solution())