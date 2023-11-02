def solution():
    
    cat_video_time = 4
    dog_video_time = cat_video_time * 2
    gorilla_video_time = (cat_video_time + dog_video_time) * 2
    total_time = cat_video_time + dog_video_time + gorilla_video_time
    result = total_time
    return result

print(solution())