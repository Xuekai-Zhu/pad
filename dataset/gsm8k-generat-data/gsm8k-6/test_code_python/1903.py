def solution():
    # Calculate the number of days in June that Allison had to upload videos
    days_in_june = 30

    # Calculate the total number of one-hour videos she uploaded in the first half of June
    half_june_videos = 10 * 15 # 15 days in half of June

    # Calculate the total number of video hours she uploaded in the first half of June 
    half_june_hours = half_june_videos * 1  # each video is one hour

    # Calculate the total number of videos she uploaded in the second half of June
    other_half_videos = 2 * half_june_videos

    # Calculate the total number of video hours she uploaded in the second half of June
    other_half_hours = other_half_videos * 1

    # Calculate the total number of video hours she uploaded in June
    total_hours = half_june_hours + other_half_hours
    result = total_hours
    return result

print(solution())