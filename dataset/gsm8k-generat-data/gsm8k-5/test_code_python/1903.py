def solution():
    videos_per_day = 10  # Allison uploads 10 videos per day
    video_duration = 1  # Each video is 1 hour long
    days_in_june = 30  # There are 30 days in June

    # Calculate the total number of video hours uploaded in the first half of June
    total_hours_first_half = (videos_per_day * video_duration * 15)

    # Double the number of video hours uploaded on the remaining days
    remaining_days = days_in_june - 15
    doubled_videos_per_day = videos_per_day * 2
    total_hours_second_half = (doubled_videos_per_day * video_duration * remaining_days)

    # Calculate the total number of video hours uploaded in June
    total_hours = total_hours_first_half + total_hours_second_half
    result = total_hours
    return result

print(solution())