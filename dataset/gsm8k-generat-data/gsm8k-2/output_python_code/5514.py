def solution():
    """There are 3 kids waiting for the swings and twice as many kids waiting for the slide. If each kid waits 2 minutes for the swings and 15 seconds for the slide, how many seconds shorter is the shorter wait?"""
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