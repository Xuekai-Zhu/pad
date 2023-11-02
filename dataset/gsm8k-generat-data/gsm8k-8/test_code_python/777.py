def solution():
    # Define the number of times Mara and Riley rode each ride
    mara_bumper_car = 2
    riley_space_shuttle = 4
    ferris_wheel = 3

    # Define the cost of each ticket
    bumper_car_cost = 2
    space_shuttle_cost = 4
    ferris_wheel_cost = 5

    # Calculate the total cost for each ride type
    bumper_car_total_cost = mara_bumper_car * bumper_car_cost
    space_shuttle_total_cost = riley_space_shuttle * space_shuttle_cost
    ferris_wheel_total_cost = ferris_wheel * ferris_wheel_cost

    # Calculate the total amount spent
    total_spent = bumper_car_total_cost + space_shuttle_total_cost + ferris_wheel_total_cost
    result = total_spent
    return result

print(solution())