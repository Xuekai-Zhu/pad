def solution():
    """John releases 3 videos on his channel a day. Two of them are short 2 minute videos and 1 of them is 6 times as long.
    Assuming a 7-day week, how many minutes of video does he release per week?"""
    # Define the length of the short videos and the length of the long video
    SHORT_VIDEO_LENGTH = 2
    LONG_VIDEO_LENGTH = 6 * 2  # 6 times as long as the short ones

    # Calculate the total length of video released per day
    daily_video_length = 2 * SHORT_VIDEO_LENGTH + LONG_VIDEO_LENGTH

    # Calculate the total length of video released per week
    weekly_video_length = daily_video_length * 7 * 3  # 7 days a week and 3 videos a day

    # Display the total length of video released per week
    result = weekly_video_length
    return result

print(solution())