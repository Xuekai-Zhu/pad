def solution():
    # Calculate the total number of photos on the first 20 pages
    photos_on_first_20_pages = 10 * 3 + 10 * 4

    # Calculate the number of remaining photos
    remaining_photos = 100 - photos_on_first_20_pages

    # Calculate the number of remaining pages
    remaining_pages = 30 - 20

    # Calculate the number of photos to be placed on each of the remaining pages
    photos_on_remaining_pages = remaining_photos / remaining_pages

    result = photos_on_remaining_pages
    return result

print(solution())