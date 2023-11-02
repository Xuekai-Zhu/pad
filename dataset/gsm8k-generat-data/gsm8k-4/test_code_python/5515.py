def solution():
    """There are 3 kids waiting for the swings and twice as many kids waiting for the slide. If each kid waits 2 minutes for the swings and 15 seconds for the slide, how many seconds shorter is the shorter wait?"""
    # Define the number of kids waiting for the swings and the slide
    swing_kids = 3
    slide_kids = 2 * swing_kids

    # Calculate the total waiting time for the swings
    swing_time = swing_kids * 2 * 60

    # Calculate the total waiting time for the slide
    slide_time = slide_kids * 15

    # Calculate the shorter wait time
    shorter_wait = abs(swing_time - slide_time)

    # return the result in seconds
    result = shorter_wait
    return result

print(solution())