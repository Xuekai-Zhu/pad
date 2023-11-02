def solution():
    """Luke takes a 70-minute bus to work every day. His coworker Paula takes 3/5 of this time to arrive by bus at work. If Luke takes a bike ride back home every day, 5 times slower than the bus, and Paula takes the bus back home, calculate the total amount of time, in minutes, they take traveling from home to work and back each day."""
    # Define the time Luke takes to travel to work by bus
    LUKE_BUS_TIME = 70

    # Define the time Paula takes to travel to work by bus
    PAULA_BUS_TIME = LUKE_BUS_TIME * (3/5)

    # Define the time Luke takes to travel back home by bike
    LUKE_BIKE_TIME = LUKE_BUS_TIME * 5

    # Define the total time Luke and Paula take to travel from home to work and back
    total_time = LUKE_BUS_TIME + PAULA_BUS_TIME + LUKE_BIKE_TIME + LUKE_BUS_TIME

    # Display the total time
    result = total_time
    return result

print(solution())