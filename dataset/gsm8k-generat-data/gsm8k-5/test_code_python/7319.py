def solution():
    initial_speed = 50  # The initial speed of the train
    initial_time = 4  # The initial time it takes the train to reach its destination

    # Calculate the new time it would take if the train traveled at 100 miles per hour
    new_time = (initial_speed / 100) * initial_time

    result = new_time
    return result

print(solution())