def solution():
    """John releases 3 videos on his channel a day. Two of them are short 2 minute videos and 1 of them is 6 times as long. Assuming a 7-day week, how many minutes of video does he release per week?"""
    # Define the length of the long video and the number of videos per day
    long_video_length = 2 * 6
    short_video_length = 2
    videos_per_day = 3

    # Calculate the total number of minutes of videos released per day
    total_minutes_per_day = (2 * short_video_length) + long_video_length

    # Calculate the total number of minutes of videos released per week
    total_minutes_per_week = total_minutes_per_day * 7 * videos_per_day

    result = total_minutes_per_week
    return result

print(solution())