def solution():
    photos = 400
    photo_size = 1.5
    video_size = 200
    drive_size = 2000
   
    used_space = photos * photo_size
    available_space = drive_size - used_space
    total_videos = available_space / video_size
    
    result = total_videos
    
    return result

print(solution())