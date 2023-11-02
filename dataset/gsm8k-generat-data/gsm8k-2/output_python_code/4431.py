def solution():
    """Shane wants to take as many photos as possible this year. He takes 146 photos in the first 2 months of the year. In January, he takes 2 photos every day. The rest of the photos were taken in February. If in February he took an equal number of photos each week, how many photos did Shane take each week in February?"""
    january_days = 31
    january_photos = 2 * january_days
    february_photos = 146 - january_photos
    february_weeks = 4
    february_photos_per_week = february_photos / february_weeks
    result = february_photos_per_week
    return result

print(solution())