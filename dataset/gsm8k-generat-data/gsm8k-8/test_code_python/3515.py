def solution():
    # Calculate the time it takes Hugo to fold a medium box
    medium_time = 3 * 2

    # Calculate the time it takes Tom to fold a small box
    small_time = 4

    # Calculate the combined time for Hugo and Tom to fold one small box
    combined_small_time = 1 / ((1 / small_time) + (1 / medium_time))

    # Calculate the combined time for Hugo and Tom to fold one medium box
    combined_medium_time = 1 / ((1 / small_time) + (1 / medium_time)) * 2

    # Calculate the total time it will take Hugo and Tom to fold 2400 small boxes and 1800 medium boxes
    total_time = (combined_small_time * 2400) + (combined_medium_time * 1800)

    result = total_time
    return result

print(solution())