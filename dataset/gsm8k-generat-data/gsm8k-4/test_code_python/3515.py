def solution():
    """Hugo can fold a small box in 3 seconds and a medium one in twice that time. Tom can fold both the small and medium boxes in 4 seconds. If Hugo and Tom want to leave as early as possible, how long (in seconds) will it take them to fold 2400 small boxes and 1800 medium boxes?"""
    # Define the time taken by Hugo to fold a small box and a medium box
    hugo_small_box_time = 3
    hugo_medium_box_time = 6

    # Define the time taken by Tom to fold both small and medium boxes
    tom_time = 4

    # Define the number of small and medium boxes to be folded
    num_small_boxes = 2400
    num_medium_boxes = 1800

    # Calculate the total time taken by Hugo to fold all small and medium boxes
    hugo_total_time = (hugo_small_box_time * num_small_boxes) + (hugo_medium_box_time * num_medium_boxes)

    # Calculate the total time taken by Tom to fold all small and medium boxes
    tom_total_time = tom_time * (num_small_boxes + num_medium_boxes)

    # Choose the shorter time between Hugo and Tom
    if hugo_total_time < tom_total_time:
        total_time = hugo_total_time
    else:
        total_time = tom_total_time

    # Return the result
    result = total_time
    return result

print(solution())