def solution():
    # Define the number of kids waiting for each ride
    swing_kids = 3
    slide_kids = 2 * swing_kids

    # Calculate the total time spent waiting for the swings
    swing_time = swing_kids * 2 * 60   # 2 minutes in seconds

    # Calculate the total time spent waiting for the slide
    slide_time = slide_kids * 15   # 15 seconds

    # Calculate the difference in wait time
    wait_time_diff = swing_time - slide_time
    result = wait_time_diff
    return result

print(solution())