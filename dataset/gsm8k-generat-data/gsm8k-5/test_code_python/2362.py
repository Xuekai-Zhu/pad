def solution():
    short_video_length = 2  # Short videos are 2 minutes long
    long_video_length = 6 * short_video_length  # Long video is 6 times as long as short videos
    daily_video_length = (2 * short_video_length) + long_video_length  # John releases 3 videos a day
    weekly_video_length = daily_video_length * 7  # John releases videos for 7 days a week

    result = weekly_video_length
    return result

print(solution())