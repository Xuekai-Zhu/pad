def solution():
    running_timeouts = 5
    throwing_timeouts = 5 * 4 - 1
    swearing_timeouts = throwing_timeouts / 3
    timeout_length = 5  # minutes

    # Calculate the total number of time-outs given
    total_timeouts = running_timeouts + throwing_timeouts + swearing_timeouts

    # Calculate the total time spent in time-out
    total_time = total_timeouts * timeout_length
    result = total_time
    return result

print(solution())