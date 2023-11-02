def solution():
    total_hours = 3 * 24  # total hours in 3 days

    # Calculate the number of complete 11-hour cycles the spaceship made
    num_full_cycles = (total_hours - 21) // 11

    # Calculate the total time the spaceship was stopped during the full cycles
    total_stopped_time = num_full_cycles * 5

    # Calculate the time stopped during the first two legs of the journey
    stopped_time = 3 + 1

    # Calculate the total time the spaceship traveled without breaks during the full cycles
    total_travel_time = num_full_cycles * 11 - stopped_time

    # Calculate the total time the spaceship was not moving during the full cycles
    total_stopped_time += stopped_time
    total_stopped_time += (total_hours - total_travel_time - 21) % 11
    result = total_stopped_time
    return result

print(solution())