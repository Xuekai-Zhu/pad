def solution():
    """There are 3 kids waiting for the swings and twice as many kids waiting for the slide. If each kid waits 2 minutes for the swings and 15 seconds for the slide, how many seconds shorter is the shorter wait?"""
    # Define the number of kids waiting for the swings and slide
    swings_kids = 3
    slide_kids = 2 * swings_kids

    # Calculate the total wait time for the swings
    swings_wait = swings_kids * 2 * 60  # 2 minutes per kid, converted to seconds

    # Calculate the total wait time for the slide
    slide_wait = slide_kids * 15  # 15 seconds per kid

    # Determine which wait time is shorter and calculate the difference
    if swings_wait < slide_wait:
        shorter_wait = "swings"
        wait_time_diff = slide_wait - swings_wait
    else:
        shorter_wait = "slide"
        wait_time_diff = swings_wait - slide_wait

    # Display the result
    result = wait_time_diff
    return result

print(solution())