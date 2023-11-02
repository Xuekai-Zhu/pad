def solution():
    # Calculate the total number of pages with 2 photos
    pages_with_2_photos = 12
    total_photos_on_2_photo_pages = pages_with_2_photos * 2

    # Calculate the total number of pages with 3 photos
    pages_with_3_photos = 9
    total_photos_on_3_photo_pages = pages_with_3_photos * 3

    # Calculate the total number of photos in the newspaper
    total_photos = total_photos_on_2_photo_pages + total_photos_on_3_photo_pages
    result = total_photos
    return result

print(solution())