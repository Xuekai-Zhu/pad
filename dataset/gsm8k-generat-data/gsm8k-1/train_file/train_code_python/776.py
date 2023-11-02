def solution():
    """Mara and Riley went to a carnival, Mara rode the bumper car two times, Riley rode the space shuttle four times, and they both rode the Ferris wheel three times. If a ticket for a bumper car cost $2, a ticket for a space shuttle cost $4, and a ticket for a Ferris wheel cost $5, how much money did they spend?"""
    bumper_car_tickets = 2
    space_shuttle_tickets = 4
    ferris_wheel_tickets = 3
    bumper_car_cost = 2
    space_shuttle_cost = 4
    ferris_wheel_cost = 5
    total_cost = (bumper_car_tickets * bumper_car_cost) + (space_shuttle_tickets * space_shuttle_cost) + (ferris_wheel_tickets * ferris_wheel_cost)
    result = total_cost
    return result

print(solution())