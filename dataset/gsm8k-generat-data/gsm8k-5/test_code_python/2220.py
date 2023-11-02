def solution():
    luke_bus_time = 70  # Luke takes a 70-minute bus to work every day
    paula_bus_time = (3/5) * luke_bus_time  # Paula takes 3/5 of Luke's bus time to arrive at work

    # Calculate the total time for Luke's daily commute
    luke_total_time = luke_bus_time + (5 * luke_bus_time)  # Luke takes a bike ride back home, which is 5 times slower than the bus

    # Calculate the total time for Paula's daily commute
    paula_total_time = paula_bus_time + luke_bus_time  # Paula takes the bus back home

    # Calculate the total amount of time they take traveling from home to work and back each day
    total_time = luke_total_time + paula_total_time
    result = total_time
    return result

print(solution())