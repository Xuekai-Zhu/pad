def solution():
    """Luke takes a 70-minute bus to work every day. His coworker Paula takes 3/5 of this time to arrive by bus at work. If Luke takes a bike ride back home every day, 5 times slower than the bus, and Paula takes the bus back home, calculate the total amount of time, in minutes, they take traveling from home to work and back each day."""
    luke_bus_time = 70
    paula_bus_time = luke_bus_time * 3/5
    luke_bike_time = luke_bus_time * 5
    total_time = luke_bus_time + paula_bus_time + luke_bike_time
    result = total_time
    return result

print(solution())