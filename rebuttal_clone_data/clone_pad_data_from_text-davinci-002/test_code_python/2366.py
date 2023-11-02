def solution():
    photos = 100
    pages = 30
    photos_on_first_ten_pages = 3 * 10
    photos_on_next_ten_pages = 4 * 10
    photos_on_last_ten_pages = (photos - photos_on_first_ten_pages - photos_on_next_ten_pages) / 10
    result = photos_on_last_ten_pages
    return result

print(solution())