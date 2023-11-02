def solution():
    
    pages_with_2_photos = 12
    pages_with_3_photos = 9
    photos_per_page_2 = 2
    photos_per_page_3 = 3
    total_photos = (pages_with_2_photos * photos_per_page_2) + (pages_with_3_photos * photos_per_page_3)
    result = total_photos
    return result

print(solution())