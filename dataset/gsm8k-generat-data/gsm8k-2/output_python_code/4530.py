def solution():
    """In a newspaper, each one of 12 pages holds 2 photos and each of another 9 pages hold 3 photos. How many photos are used in the newspaper?"""
    pages_with_2_photos = 12
    pages_with_3_photos = 9
    photos_per_page_2 = 2
    photos_per_page_3 = 3
    total_photos = (pages_with_2_photos * photos_per_page_2) + (pages_with_3_photos * photos_per_page_3)
    result = total_photos
    return result

print(solution())