def solution():
    swings_kids = 3  # 3 kids waiting for the swings
    slide_kids = 2 * swings_kids  # Twice as many kids waiting for the slide
    swing_wait_time = 2  # Each kid waits for 2 minutes for the swings
    slide_wait_time = 15  # Each kid waits for 15 seconds for the slide

    # Calculate total wait time for the swings and the slide
    total_swings_wait_time = swings_kids * swing_wait_time * 60  # Convert minutes to seconds
    total_slide_wait_time = slide_kids * slide_wait_time

    # Calculate the difference in wait time
    difference = total_swings_wait_time - total_slide_wait_time
    result = difference
    return result

print(solution())