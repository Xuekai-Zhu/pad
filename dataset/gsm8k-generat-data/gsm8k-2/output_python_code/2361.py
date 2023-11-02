def solution():
    """John releases 3 videos on his channel a day. Two of them are short 2 minute videos and 1 of them is 6 times as long. Assuming a 7-day week, how many minutes of video does he release per week?"""
    short_video_length = 2
    long_video_length = 6 * short_video_length
    videos_per_day = 3
    short_videos_per_day = 2
    long_video_per_day = 1
    total_videos_per_week = videos_per_day * 7
    total_short_videos_per_week = short_videos_per_day * 7
    total_long_videos_per_week = long_video_per_day * 7
    total_short_video_length = total_short_videos_per_week * short_video_length
    total_long_video_length = total_long_videos_per_week * long_video_length
    total_video_length = total_short_video_length + total_long_video_length
    result = total_video_length
    return result

print(solution())