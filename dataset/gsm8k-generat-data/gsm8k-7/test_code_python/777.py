def solution():
    bumper_car_tickets = 2  # in dollars
    space_shuttle_tickets = 4  # in dollars
    ferris_wheel_tickets = 5  # in dollars

    mara_bumper_car_rides = 2
    riley_space_shuttle_rides = 4
    collective_ferris_wheel_rides = 6

    # Calculate the total cost of all bumper car tickets purchased by Mara and Riley
    total_bumper_car_cost = mara_bumper_car_rides * bumper_car_tickets

    # Calculate the total cost of all space shuttle tickets purchased by Mara and Riley
    total_space_shuttle_cost = riley_space_shuttle_rides * space_shuttle_tickets

    # Calculate the total cost of all Ferris wheel tickets purchased by Mara and Riley
    total_ferris_wheel_cost = collective_ferris_wheel_rides * ferris_wheel_tickets

    # Calculate the total amount of money spent by Mara and Riley at the carnival
    total_cost = total_bumper_car_cost + total_space_shuttle_cost + total_ferris_wheel_cost
    result = total_cost
    return result

print(solution())