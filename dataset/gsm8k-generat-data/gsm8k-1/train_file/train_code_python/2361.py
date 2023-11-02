def solution():
    """John releases 3 videos on his channel a day. Two of them are short 2 minute videos and 1 of them is 6 times as long. Assuming a 7-day week, how many minutes of video does he release per week?"""
    short_videos = 2
    long_video = 6 * short_videos
    videos_per_day = short_videos + 1
    days_per_week = 7
    total_videos = videos_per_day * days_per_week
    total_minutes = (short_videos * 2 + long_video) * total_videos
    result = total_minutes
    return result

print(solution())