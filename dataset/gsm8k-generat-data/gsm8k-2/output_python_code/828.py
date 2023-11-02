def solution():
    """Jeanne wants to ride the Ferris wheel, the roller coaster, and the bumper cars. The Ferris wheel costs 5 tickets, the roller coaster costs 4 tickets and the bumper cars cost 4 tickets. Jeanne has 5 tickets. How many more tickets should Jeanne buy?"""
    ferris_wheel_tickets = 5
    roller_coaster_tickets = 4
    bumper_cars_tickets = 4
    total_tickets_needed = ferris_wheel_tickets + roller_coaster_tickets + bumper_cars_tickets
    remaining_tickets = total_tickets_needed - 5
    result = remaining_tickets
    return result

print(solution())