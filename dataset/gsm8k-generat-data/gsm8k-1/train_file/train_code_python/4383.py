def solution():
    """For every 100 additional people that board a spaceship, its speed is halved. If the speed of the spaceship with 200 people on board is 500km per hour, what is its speed in km/hr when there are 400 people on board?"""
    base_speed = 500
    base_capacity = 200
    additional_capacity = 100
    passenger_count = 400
    capacity_difference = (passenger_count - base_capacity) // additional_capacity
    final_speed = base_speed / (2 ** capacity_difference)
    result = final_speed
    return result

print(solution())