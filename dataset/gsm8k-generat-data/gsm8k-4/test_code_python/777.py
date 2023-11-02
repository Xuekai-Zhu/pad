def solution():
    """Mara and Riley went to a carnival, Mara rode the bumper car two times, Riley rode the space shuttle four times, and they both rode the Ferris wheel three times. If a ticket for a bumper car cost $2, a ticket for a space shuttle cost $4, and a ticket for a Ferris wheel cost $5, how much money did they spend?"""
    # Define the number of times Mara and Riley rode the rides
    bumper_car_rides = 2
    space_shuttle_rides = 4
    ferris_wheel_rides = 3

    # Define the prices of each ride
    bumper_car_price = 2
    space_shuttle_price = 4
    ferris_wheel_price = 5

    # Calculate the total amount spent
    total_spent = (bumper_car_rides * bumper_car_price) + (space_shuttle_rides * space_shuttle_price) + (ferris_wheel_rides * ferris_wheel_price)

    # return the result
    result = total_spent
    return result

print(solution())