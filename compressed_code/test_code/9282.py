def solution():
    
    january_photos = 2 * 31
    total_photos = 146 - january_photos
    february_photos = total_photos
    photos_per_week = february_photos / 4
    result = photos_per_week
    return result

print(solution())