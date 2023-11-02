def solution():
    
    first_video_length = 2 * 60
    second_video_length = 4 * 60 + 30
    total_length = 510
    last_two_videos_length = (total_length - first_video_length - second_video_length) / 2
    result = last_two_videos_length
    return result

print(solution())