def solution():
    # Calculate the total length of time Kimiko spent watching the last two videos
    total_time = 510 - (2*60) - (4*60 + 30)  # convert minutes to seconds
    minutes_per_video = total_time / 2
    seconds_per_video = minutes_per_video * 60
    result = seconds_per_video
    return result

print(solution())