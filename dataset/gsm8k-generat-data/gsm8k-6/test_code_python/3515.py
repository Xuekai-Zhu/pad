def solution():
    # Calculate the time it takes for Hugo to fold a small box and a medium box
    time_small = 3
    time_medium = 6  # medium box takes twice as long as small box

    # Calculate the time it takes for Tom to fold a small box and a medium box
    time_tom = 4

    # Calculate the number of boxes each person can fold per second
    rate_hugo_small = 1/time_small
    rate_hugo_medium = 1/time_medium
    rate_tom_small = 1/time_tom
    rate_tom_medium = 1/time_tom

    # Calculate the total time it will take Hugo and Tom to fold 2400 small boxes and 1800 medium boxes
    total_boxes = 2400 + 1800
    total_time_hugo = total_boxes * (rate_hugo_small + rate_hugo_medium)
    total_time_tom = total_boxes * (rate_tom_small + rate_tom_medium)

    # Choose the minimum time between Hugo and Tom
    result = min(total_time_hugo, total_time_tom)
    return result

print(solution())