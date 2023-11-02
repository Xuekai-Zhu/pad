def solution():
    """Jeanne wants to ride the Ferris wheel, the roller coaster, and the bumper cars. The Ferris wheel costs 5 tickets, the roller coaster costs 4 tickets and the bumper cars cost 4 tickets. Jeanne has 5 tickets. How many more tickets should Jeanne buy?"""
    tickets_owned = 5
    ferris_wheel_cost = 5
    roller_coaster_cost = 4
    bumper_cars_cost = 4
    total_cost = ferris_wheel_cost + roller_coaster_cost + bumper_cars_cost
    tickets_needed = total_cost - tickets_owned
    result = tickets_needed
    return result

print(solution())