def solution():
    """Alyssa took 100 photos on vacation. She wants to put them in a photo album with 30 pages. She can place 3 photos each on the first 10 pages. Then she can place 4 photos each on the next 10 pages. If she wants to put an equal number of photos on each of the remaining pages of the album, how many photos can she place on each page?"""
    # Define the total number of photos and pages
    total_photos = 100
    total_pages = 30

    # Calculate the number of photos already placed in the album
    placed_photos = 10 * 3 + 10 * 4

    # Calculate the number of remaining pages
    remaining_pages = total_pages - 20

    # Calculate the number of remaining photos
    remaining_photos = total_photos - placed_photos

    # Calculate the number of photos to be placed on each of the remaining pages
    photos_per_page = remaining_photos / remaining_pages

    # return the result
    result = int(photos_per_page)
    return result

print(solution())