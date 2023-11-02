def solution():
    total_time = 510  # seconds
    time_first_video = 2  # minutes
    time_second_video = 4*60 + 30  # seconds

    # Calculate the total time of the first two videos in seconds
    total_time_first_two = time_first_video * 60 + time_second_video

    # Calculate the total time of the last two videos in seconds
    total_time_last_two = total_time - total_time_first_two

    # Calculate the length of each of the last two videos in seconds
    length_last_two = total_time_last_two / 2

    result = length_last_two
    return result

print(solution())