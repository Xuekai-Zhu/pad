def solution():
    """Jeanne wants to ride the Ferris wheel, the roller coaster, and the bumper cars. The Ferris wheel costs 5 tickets, the roller coaster costs 4 tickets and the bumper cars cost 4 tickets. Jeanne has 5 tickets. How many more tickets should Jeanne buy?"""
    # Define the ticket costs and the number of tickets Jeanne has
    FERRIS_WHEEL_TICKET_COST = 5
    ROLLER_COASTER_TICKET_COST = 4
    BUMPER_CARS_TICKET_COST = 4
    JEANNE_TICKETS = 5

    # Calculate the total cost of the rides
    total_cost = FERRIS_WHEEL_TICKET_COST + ROLLER_COASTER_TICKET_COST + BUMPER_CARS_TICKET_COST

    # Calculate the number of tickets Jeanne needs to buy
    tickets_needed = total_cost - JEANNE_TICKETS

    result = tickets_needed
    return result

print(solution())