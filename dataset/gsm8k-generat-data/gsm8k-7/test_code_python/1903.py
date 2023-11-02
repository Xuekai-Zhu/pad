def solution():
    num_videos_per_day = 10
    hours_per_video = 1
    num_days_in_month = 30

    # Calculate the total number of hours of video Allison uploaded in the first half of June
    first_half_hours = num_videos_per_day * hours_per_video * (num_days_in_month / 2)

    # Calculate the total number of videos Allison uploaded in the second half of June
    num_videos_second_half = num_videos_per_day * (num_days_in_month / 2)

    # Double the number of hours per video for the second half of June
    doubled_hours_per_video = hours_per_video * 2

    # Calculate the total number of hours of video Allison uploaded in the second half of June
    second_half_hours = num_videos_second_half * doubled_hours_per_video

    # Calculate the total number of hours of video Allison uploaded in the entire month
    total_hours = first_half_hours + second_half_hours
    result = total_hours
    return result

print(solution())