def solution():
    """There are 3 kids waiting for the swings and twice as many kids waiting for the slide. If each kid waits 2 minutes for the swings and 15 seconds for the slide, how many seconds shorter is the shorter wait?"""
    swings_kids = 3
    slide_kids = swings_kids * 2
    swings_wait_time = 2 * 60  # 2 minutes in seconds
    slide_wait_time = 15  # 15 seconds
    total_swings_wait_time = swings_kids * swings_wait_time
    total_slide_wait_time = slide_kids * slide_wait_time
    shorter_wait_time = total_slide_wait_time - total_swings_wait_time
    result = shorter_wait_time
    return result

print(solution())