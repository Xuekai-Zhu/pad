def solution():
    """Mara and Riley went to a carnival, Mara rode the bumper car two times, Riley rode the space shuttle four times, and they both rode the Ferris wheel three times. If a ticket for a bumper car cost $2, a ticket for a space shuttle cost $4, and a ticket for a Ferris wheel cost $5, how much money did they spend?"""
    # Define the prices for each ride
    BUMPER_CAR_PRICE = 2
    SPACE_SHUTTLE_PRICE = 4
    FERRIS_WHEEL_PRICE = 5

    # Define the number of times each ride was taken
    bumper_car_times = 2
    space_shuttle_times = 4
    ferris_wheel_times = 3

    # Calculate the total cost for Mara and Riley
    mara_cost = (bumper_car_times + ferris_wheel_times) * BUMPER_CAR_PRICE + ferris_wheel_times * FERRIS_WHEEL_PRICE
    riley_cost = space_shuttle_times * SPACE_SHUTTLE_PRICE + ferris_wheel_times * FERRIS_WHEEL_PRICE
    total_cost = mara_cost + riley_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())