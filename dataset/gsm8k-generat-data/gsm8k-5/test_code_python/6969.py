def solution():
    rollercoaster_rides = 3
    catapult_rides = 2
    ferris_wheel_rides = 1

    rollercoaster_cost = 4
    catapult_cost = 4
    ferris_wheel_cost = 1

    # Calculate total cost of rides in terms of tickets
    total_cost = (rollercoaster_rides * rollercoaster_cost) + (catapult_rides * catapult_cost) + (
            ferris_wheel_rides * ferris_wheel_cost)
    result = total_cost
    return result

print(solution())