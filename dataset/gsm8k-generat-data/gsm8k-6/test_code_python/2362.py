def solution():
    # Calculate the total minutes of video released by John in a week
    short_video_time = 2 * 2  # each short video is 2 minutes
    long_video_time = 6 * short_video_time  # the long video is 6 times as long as the short videos
    total_video_time_per_day = short_video_time * 2 + long_video_time  # John releases 3 videos a day
    total_video_time_per_week = total_video_time_per_day * 7  # a week has 7 days
    result = total_video_time_per_week
    return result

print(solution())