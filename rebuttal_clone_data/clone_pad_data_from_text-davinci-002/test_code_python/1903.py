def solution():
    videos_per_day = 10
    video_hours_per_day = 1
    days_in_month = 30
    total_video_hours = (videos_per_day * video_hours_per_day) + ((days_in_month - 15) * (videos_per_day * 2 * video_hours_per_day))
    result = total_video_hours
    return result

print(solution())