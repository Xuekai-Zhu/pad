def solution():
    # Calculate the time it takes for the elevator to reach the ground floor
    elevator_time = 60

    # Calculate the number of floors Austin descends
    austin_floors = 9

    # Calculate the total time it takes Austin to reach the ground floor
    austin_time = elevator_time

    # Calculate the number of steps Jake descends
    jake_steps_per_floor = 30 * 3
    jake_steps = jake_steps_per_floor * (austin_floors - 1) + 30

    # Calculate the time it takes Jake to descend the stairs
    jake_time = jake_steps / 3

    # Calculate the time difference between Jake and Austin
    time_difference = jake_time - austin_time

    result = time_difference
    return result

print(solution())