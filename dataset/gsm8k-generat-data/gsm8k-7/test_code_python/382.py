def solution():
    num_windows = 64
    num_windows_per_cycle = 4
    time_per_cycle = 10 # in minutes

    # Calculate the number of cycles David needs to wash all windows
    num_cycles = num_windows / num_windows_per_cycle

    # Calculate the total time needed to wash all windows
    total_time = num_cycles * time_per_cycle
    result = total_time
    return result

print(solution())