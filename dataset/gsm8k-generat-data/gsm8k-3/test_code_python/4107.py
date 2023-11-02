def solution():
    """Kimiko watches four YouTube videos. The first video is 2 minutes long, the second video is 4 minutes and 30 seconds, and the last two videos are equal in length. If she spends a total of 510 seconds watching YouTube, how many seconds long was each of the last two videos?"""
    # Convert the length of the second video to seconds
    video2_length = 4 * 60 + 30

    # Calculate the total length of the first three videos
    total_length = 2 * 60 + video2_length

    # Calculate the length of each of the last two videos
    last_videos_length = (510 - total_length) / 2

    # Display the length of each of the last two videos
    result = last_videos_length
    return result

print(solution())