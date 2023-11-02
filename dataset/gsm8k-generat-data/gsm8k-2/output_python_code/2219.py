def solution():
    """Luke takes a 70-minute bus to work every day. His coworker Paula takes 3/5 of this time to arrive by bus at work. If Luke takes a bike ride back home every day, 5 times slower than the bus, and Paula takes the bus back home, calculate the total amount of time, in minutes, they take traveling from home to work and back each day."""

    bus_time_to_work = 70
    paula_time_to_work = (3 / 5) * bus_time_to_work
    bus_time_to_home = bus_time_to_work
    bike_time_to_home = bus_time_to_work * 5
    total_time_each_day = bus_time_to_work + paula_time_to_work + bus_time_to_home + bike_time_to_home

    result = total_time_each_day
    return result

print(solution())