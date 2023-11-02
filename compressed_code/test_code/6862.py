def solution():
    
    storage_space = 2000 * 1.5
    space_used_by_photos = 400 * 1.5
    available_space = storage_space - space_used_by_photos
    video_size = 200
    videos_stored = available_space // video_size
    result = videos_stored
    return result

print(solution())