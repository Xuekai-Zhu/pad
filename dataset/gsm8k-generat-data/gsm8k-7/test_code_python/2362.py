def solution():
    daily_short_videos = 2  # in minutes
    daily_long_video = 2 * 6  # in minutes
    num_days = 7

    # Calculate the total minutes of short videos released for the week
    total_short_videos = daily_short_videos * num_days * 2  # 2 short videos per day

    # Calculate the total minutes of the long video released for the week
    total_long_video = daily_long_video * num_days

    # Calculate the total minutes of video released for the week
    total_video = total_short_videos + total_long_video
    result = total_video
    return result

print(solution())