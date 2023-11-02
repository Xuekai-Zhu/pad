def solution():
    # Calculate the length of the long video in minutes
    long_video_length = 2 * 6

    # Calculate the total minutes of video released per day
    daily_minutes = (2 * 2) + long_video_length

    # Calculate the total minutes of video released per week
    weekly_minutes = daily_minutes * 7

    result = weekly_minutes
    return result

print(solution())