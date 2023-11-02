def solution():
    total_photos = 100  # Alyssa took 100 photos
    total_pages = 30  # Alyssa wants to put the photos in a 30-page album
    photos_per_page_first_10 = 3  # Alyssa can place 3 photos on each of the first 10 pages
    photos_per_page_next_10 = 4  # Alyssa can place 4 photos on each of the next 10 pages

    # Calculate the total number of pages used for the first 20 photos
    pages_for_first_20 = 10 + 10*(photos_per_page_next_10/photos_per_page_first_10)
    remaining_pages = total_pages - pages_for_first_20  # Alyssa has to use the remaining pages

    # Calculate the number of photos Alyssa can place on each of the remaining pages
    photos_remaining = total_photos - 20*(photos_per_page_first_10) - 10*(photos_per_page_next_10)
    photos_per_page_remaining = photos_remaining / remaining_pages
    result = photos_per_page_remaining
    return result

print(solution())