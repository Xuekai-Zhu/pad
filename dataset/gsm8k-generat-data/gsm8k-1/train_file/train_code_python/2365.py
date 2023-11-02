def solution():
    """Alyssa took 100 photos on vacation. She wants to put them in a photo album with 30 pages. She can place 3 photos each on the first 10 pages. Then she can place 4 photos each on the next 10 pages. If she wants to put an equal number of photos on each of the remaining pages of the album, how many photos can she place on each page?"""
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