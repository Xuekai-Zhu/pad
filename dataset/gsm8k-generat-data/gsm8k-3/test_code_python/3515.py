def solution():
    """Hugo can fold a small box in 3 seconds and a medium one in twice that time. Tom can fold both the small and medium boxes in 4 seconds. If Hugo and Tom want to leave as early as possible, how long (in seconds) will it take them to fold 2400 small boxes and 1800 medium boxes?"""
    # Define the time it takes to fold a small box and a medium box for Hugo
    HUGO_SMALL_TIME = 3
    HUGO_MEDIUM_TIME = 6

    # Define the time it takes to fold both types of boxes for Tom
    TOM_TIME = 4

    # Define the number of small and medium boxes to be folded
    small_boxes = 2400
    medium_boxes = 1800

    # Calculate the total time it would take Hugo to fold all the small and medium boxes separately
    hugo_total_time = (small_boxes * HUGO_SMALL_TIME) + (medium_boxes * HUGO_MEDIUM_TIME)

    # Calculate the total time it would take Tom to fold all the boxes
    tom_total_time = (small_boxes + medium_boxes) * TOM_TIME

    # Determine who would take less time and add up their times accordingly
    if hugo_total_time <= tom_total_time:
        result = hugo_total_time
    else:
        # Calculate the time it would take for Tom to fold all the small boxes
        tom_small_time = (small_boxes * 2) * TOM_TIME  # Tom takes twice as long as Hugo for a medium box
        # Add up the time it takes for Tom to fold all the small and medium boxes
        result = tom_small_time + (medium_boxes * TOM_TIME)

    return result

print(solution())