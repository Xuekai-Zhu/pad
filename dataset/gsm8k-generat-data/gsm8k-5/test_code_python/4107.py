def solution():
    total_length = 2*60 + 4*60 + 30  # Total length of the first three videos in seconds
    remaining_length = 510 - total_length  # Length of the last two videos in seconds

    # Divide the remaining length equally between the last two videos
    length_last_two_videos = remaining_length / 2
    result = length_last_two_videos
    return result

print(solution())