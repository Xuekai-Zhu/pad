def solution():
    
    swings_wait_time = 2 * 60
    slide_wait_time = 15
    number_of_swings_kids = 3
    number_of_slide_kids = 6
    total_swings_wait_time = swings_wait_time * number_of_swings_kids
    total_slide_wait_time = slide_wait_time * number_of_slide_kids
    shorter_wait_time = total_swings_wait_time - total_slide_wait_time
    result = shorter_wait_time
    return result

print(solution())