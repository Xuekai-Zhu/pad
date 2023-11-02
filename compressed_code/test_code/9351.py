def solution():
    
    pages_with_two_photos = 12
    pages_with_three_photos = 9
    photos_on_each_page_with_two_photos = 2
    photos_on_each_page_with_three_photos = 3
    total_photos = (pages_with_two_photos * photos_on_each_page_with_two_photos) + (pages_with_three_photos * photos_on_each_page_with_three_photos)
    result = total_photos
    return result

print(solution())