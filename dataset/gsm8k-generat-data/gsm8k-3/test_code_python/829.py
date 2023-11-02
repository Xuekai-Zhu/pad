def solution():
    """Jeanne wants to ride the Ferris wheel, the roller coaster, and the bumper cars. The Ferris wheel costs 5 tickets, the roller coaster costs 4 tickets and the bumper cars cost 4 tickets. Jeanne has 5 tickets. How many more tickets should Jeanne buy?"""
    # Define the cost of each ride in tickets
    FERRIS_WHEEL_COST = 5
    ROLLER_COASTER_COST = 4
    BUMPER_CARS_COST = 4

    # Define the number of tickets Jeanne has
    tickets = 5

    # Calculate the total cost of the rides
    total_cost = FERRIS_WHEEL_COST + ROLLER_COASTER_COST + BUMPER_CARS_COST

    # Calculate the number of tickets Jeanne needs to buy
    tickets_needed = total_cost - tickets

    # Display the number of tickets Jeanne needs to buy
    result = tickets_needed
    return result

print(solution())