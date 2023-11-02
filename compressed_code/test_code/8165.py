def solution():
    
    video_length = 100
    lila_speed = 2
    roger_speed = 1
    num_videos = 6
    total_hours = (video_length/lila_speed + video_length/roger_speed) * num_videos
    result = total_hours
    return result

print(solution())