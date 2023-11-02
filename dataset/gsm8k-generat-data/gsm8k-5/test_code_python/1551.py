def solution():
    time_out_running = 5
    time_out_throwing_food = (5 * 5) - 1
    time_out_swearing = time_out_throwing_food / 3

    total_time_outs = time_out_running + time_out_throwing_food + time_out_swearing
    time_spent_in_time_out = total_time_outs * 5  # each time-out is 5 minutes

    result = time_spent_in_time_out
    return result

print(solution())