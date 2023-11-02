def solution():
    
    cat_video_duration = 4
    dog_video_duration = cat_video_duration * 2
    gorilla_video_duration = (cat_video_duration + dog_video_duration) * 2
    total_video_duration = cat_video_duration + dog_video_duration + gorilla_video_duration
    result = total_video_duration
    return result

print(solution())