def solution():
    
    total_photos = 100
    pages = 30
    first_ten_pages_photos = 3 * 10
    next_ten_pages_photos = 4 * 10
    remaining_photos = total_photos - first_ten_pages_photos - next_ten_pages_photos
    remaining_pages = pages - 20
    equal_photos_per_page = remaining_photos / remaining_pages
    result = equal_photos_per_page
    return result

print(solution())