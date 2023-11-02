def solution():
    """James decides to go to prom with Susan.  He pays for everything.  The tickets cost $100 each. Dinner is $120.  He leaves a 30% tip.  He also charters a limo for 6 hours that cost $80 per hour.  How much did it all cost? """
    # Define the costs of each item
    TICKET_COST = 100
    DINNER_COST = 120
    TIP_PERCENTAGE = 0.3
    LIMO_COST_PER_HOUR = 80
    LIMO_HOURS = 6

    # Calculate the total cost of the tickets
    ticket_total = 2 * TICKET_COST

    # Calculate the total cost of dinner
    dinner_total = DINNER_COST + (DINNER_COST * TIP_PERCENTAGE)

    # Calculate the cost of the limo rental
    limo_total = LIMO_HOURS * LIMO_COST_PER_HOUR

    # Calculate the total cost of everything
    total_cost = ticket_total + dinner_total + limo_total

    # Display the total cost
    result = total_cost
    return result

print(solution())