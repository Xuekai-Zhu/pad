def solution():
    """Allison, a YouTuber, uploads 10 one-hour videos of food reviews each day to her channel. She uploaded videos halfway through June, at that pace, and then doubled the number of video hours she uploaded on the remaining days. What's the total number of video hours she has uploaded at the end of the month?"""
    days_in_june = 30
    videos_per_day = 10
    video_hours_per_day = videos_per_day * 1 # each video is one hour
    first_half_of_month = days_in_june // 2
    video_hours_first_half = first_half_of_month * video_hours_per_day
    remaining_days = days_in_june - first_half_of_month
    doubled_video_hours_per_day = video_hours_per_day * 2
    video_hours_remaining_days = doubled_video_hours_per_day * remaining_days
    total_video_hours = video_hours_first_half + video_hours_remaining_days
    result = total_video_hours
    return result

print(solution())