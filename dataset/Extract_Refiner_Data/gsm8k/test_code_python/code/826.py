def solution():
    
    # Define the number of videos and the duration of each video
    videos_per_week = 18
    video_duration = 4

    # Calculate the total duration of TikTok videos per week
    total_duration = videos_per_week * video_duration * 7

    # Calculate the total duration of TikTok's makeup per week
    makeup_duration = 15 * 6

    # Calculate the total duration of TikTok's makeup per week
    total_makeup_duration = makeup_duration * 7

    # Calculate the total duration of TikTok's makeup per week
    total_duration += total_makeup_duration

    # Calculate the total duration of TikTok's tikTok in a month
    monthly_duration = total_duration * 4

    # return the result
    result = monthly_duration
    return result

print(solution())