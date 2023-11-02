def solution():
    
    total_photo_storage = 2000 * 1.5
    remaining_storage = total_photo_storage - (400 * 1.5)
    video_size = 200
    videos = remaining_storage // video_size
    result = videos
    return result

print(solution())