def solution():
    """Kimiko watches four YouTube videos. The first video is 2 minutes long,
    the second video is 4 minutes and 30 seconds, and the last two videos are
    equal in length. If she spends a total of 510 seconds watching YouTube, how
    many seconds long was each of the last two videos?"""
    first_video_length = 2 * 60
    second_video_length = 4 * 60 + 30
    total_length = 510
    last_two_videos_length = (total_length - first_video_length - second_video_length) / 2
    result = last_two_videos_length
    return result

print(solution())