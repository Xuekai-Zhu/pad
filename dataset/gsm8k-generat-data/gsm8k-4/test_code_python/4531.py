def solution():
    """In a newspaper, each one of 12 pages holds 2 photos and each of another 9 pages hold 3 photos. How many photos are used in the newspaper?"""
    # Calculate the total number of photos on the pages with 2 photos each
    pages_with_2_photos = 12
    photos_on_2_pages = pages_with_2_photos * 2

    # Calculate the total number of photos on the pages with 3 photos each
    pages_with_3_photos = 9
    photos_on_3_pages = pages_with_3_photos * 3

    # Calculate the total number of photos in the newspaper
    total_photos = photos_on_2_pages + photos_on_3_pages

    # return the result
    result = total_photos
    return result

print(solution())