def solution():
    timeouts_for_running = 5
    timeouts_for_throwing_food = timeouts_for_running - 1
    timeouts_for_swearing = timeouts_for_throwing_food / 3
    total_timeouts = timeouts_for_running + timeouts_for_throwing_food + timeouts_for_swearing
    timeout_length = 5
    total_timeout_length = total_timeouts * timeout_length
    result = total_timeout_length
    return result

print(solution())