def solution():
    
    total_photos = 100
    pages_with_3_photos = 10
    pages_with_4_photos = 10
    remaining_pages = 30 - pages_with_3_photos - pages_with_4_photos
    remaining_photos = total_photos - (pages_with_3_photos * 3) - (pages_with_4_photos * 4)
    photos_per_page = remaining_photos / remaining_pages
    result = photos_per_page
    return result

print(solution())