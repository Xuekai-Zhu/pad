def solution():
    
    january_days = 31
    january_photos = 2 * january_days
    february_photos = 146 - january_photos
    february_weeks = 4
    february_photos_per_week = february_photos / february_weeks
    result = february_photos_per_week
    return result

print(solution())