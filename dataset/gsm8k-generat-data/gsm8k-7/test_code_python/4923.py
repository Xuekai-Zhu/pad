def solution():
    num_floors = 9
    steps_per_floor = 30
    steps_per_second = 3
    elevator_time = 60    # in seconds

    # Calculate the total number of steps that Austin needs to descend
    total_steps_austin = num_floors * steps_per_floor

    # Calculate the time it takes for Austin to descend using the elevator
    austin_time = elevator_time

    # Calculate the total time it takes for Jake to descend using the stairs
    jake_time = (total_steps_austin // steps_per_second) + 1   # add 1 second for going from 9th floor to ground level

    # Calculate the time difference between Jake and Austin
    time_diff = jake_time - austin_time
    result = time_diff
    return result

print(solution())