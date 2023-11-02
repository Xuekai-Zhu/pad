def solution():
    """Mara and Riley went to a carnival, Mara rode the bumper car two times, Riley rode the space shuttle four times, and they both rode the Ferris wheel three times. If a ticket for a bumper car cost $2, a ticket for a space shuttle cost $4, and a ticket for a Ferris wheel cost $5, how much money did they spend?"""
    mara_bumper_car = 2
    riley_space_shuttle = 4
    total_ferris_wheel = 3 * 2  # they both rode it three times
    bumper_car_cost = 2
    space_shuttle_cost = 4
    ferris_wheel_cost = 5
    total_cost = (mara_bumper_car * bumper_car_cost) + (riley_space_shuttle * space_shuttle_cost) + (
                total_ferris_wheel * ferris_wheel_cost)
    result = total_cost
    return result

print(solution())