def solution():
    num_small_boxes = 2400
    num_medium_boxes = 1800

    h_small_time = 3  # time for Hugo to fold a small box
    h_medium_time = h_small_time * 2  # time for Hugo to fold a medium box

    st_small_time = 4  # time for Tom to fold a small box
    st_medium_time = 4  # time for Tom to fold a medium box

    # Calculate Hugo's total time to fold all small boxes
    h_total_small_time = num_small_boxes * h_small_time

    # Calculate Hugo's total time to fold all medium boxes
    h_total_medium_time = num_medium_boxes * h_medium_time

    # Calculate Tom's total time to fold all small and medium boxes
    st_total_time = (num_small_boxes + num_medium_boxes) * st_small_time

    # Find the minimum time by considering both Hugo and Tom's time
    min_time = max(h_total_small_time, h_total_medium_time, st_total_time)

    result = min_time
    return result

print(solution())