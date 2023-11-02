def solution():
    """Alyssa took 100 photos on vacation. She wants to put them in a photo album with 30 pages. She can place 3 photos each on the first 10 pages. Then she can place 4 photos each on the next 10 pages. If she wants to put an equal number of photos on each of the remaining pages of the album, how many photos can she place on each page?"""
    total_photos = 100
    pages_with_3_photos = 10
    pages_with_4_photos = 10
    remaining_pages = 30 - pages_with_3_photos - pages_with_4_photos
    remaining_photos = total_photos - (pages_with_3_photos * 3) - (pages_with_4_photos * 4)
    photos_per_page = remaining_photos / remaining_pages
    result = photos_per_page
    return result

print(solution())