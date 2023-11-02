def solution():
    """Luke takes a 70-minute bus to work every day. His coworker Paula takes 3/5 of this time to arrive by bus at work. If Luke takes a bike ride back home every day, 5 times slower than the bus, and Paula takes the bus back home, calculate the total amount of time, in minutes, they take traveling from home to work and back each day."""
    # Define the time taken by Luke in each direction
    luke_to_work = 70
    luke_to_home = luke_to_work * 5

    # Define the time taken by Paula in each direction
    paula_to_work = luke_to_work * (3/5)
    paula_to_home = luke_to_work * (2/5)

    # Calculate the total time taken by both of them each day
    total_time = luke_to_work + paula_to_work + luke_to_home + paula_to_home

    result = total_time
    return result

print(solution())