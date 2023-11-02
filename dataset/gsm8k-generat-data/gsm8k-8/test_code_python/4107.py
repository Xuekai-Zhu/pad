def solution():
    # Convert the length of the second video to seconds
    second_video_length = 4*60 + 30

    # Calculate the total length of the first three videos
    first_three_videos_length = 2 + second_video_length

    # Calculate the length of the last two videos
    last_two_videos_length = (510 - first_three_videos_length) / 2

    result = last_two_videos_length
    return result

print(solution())