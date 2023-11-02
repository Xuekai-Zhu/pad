def solution():
    """Shane wants to take as many photos as possible this year. He takes 146 photos in the first 2 months of the year. In January, he takes 2 photos every day. The rest of the photos were taken in February. If in February he took an equal number of photos each week, how many photos did Shane take each week in February?"""
    january_photos = 2 * 31
    total_photos = 146 - january_photos
    february_photos = total_photos
    photos_per_week = february_photos / 4
    result = photos_per_week
    return result

print(solution())