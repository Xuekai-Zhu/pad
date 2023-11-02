def solution():
    total_training_time = 5 * 60  # total training time in minutes
    multiplication_time = 10  # time spent on multiplication problems in minutes
    division_time = 20  # time spent on division problems in minutes

    # Calculate the total time it takes to complete one cycle of multiplication and division problems
    total_cycle_time = multiplication_time + division_time

    # Calculate the number of cycles that can be completed in the total training time
    num_cycles = total_training_time // total_cycle_time

    # If there is any remaining time, add an extra cycle
    if total_training_time % total_cycle_time != 0:
        num_cycles += 1

    # Calculate the number of days needed to complete the training
    num_days = num_cycles / 2
    result = num_days
    return result

print(solution())