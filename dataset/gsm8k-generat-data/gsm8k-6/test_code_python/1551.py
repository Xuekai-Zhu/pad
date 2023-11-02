def solution():
    # Calculate the number of time-outs for running
    time_outs_running = 5

    # Calculate the number of time-outs for throwing food
    time_outs_food = 5 * time_outs_running - 1

    # Calculate the number of time-outs for swearing
    time_outs_swearing = time_outs_food / 3

    # Calculate the total time in time-out
    total_time_out = (time_outs_running + time_outs_food + time_outs_swearing) * 5  # each time-out is 5 minutes
    result = total_time_out
    return result

print(solution())