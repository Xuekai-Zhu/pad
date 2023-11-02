def solution():
    num_swings_wait = 3
    num_slide_wait = 2 * num_swings_wait
    
    wait_time_swings_sec = 120
    wait_time_slide_sec = 15
    
    total_wait_swings_sec = num_swings_wait * wait_time_swings_sec
    total_wait_slide_sec = num_slide_wait * wait_time_slide_sec
    
    shorter_wait_sec = total_wait_slide_sec - total_wait_swings_sec
    result = shorter_wait_sec
    return result

print(solution())