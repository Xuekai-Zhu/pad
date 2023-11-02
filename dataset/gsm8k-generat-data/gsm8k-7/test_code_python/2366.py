def solution():
    total_photos = 100
    num_pages = 30

    # Calculate the total number of photos that can be placed on the first 10 pages
    num_photos_first_10_pages = 3 * 10

    # Calculate the total number of photos that can be placed on the next 10 pages
    num_photos_next_10_pages = 4 * 10

    # Calculate the remaining number of photos after placing them on the first 20 pages
    remaining_photos = total_photos - num_photos_first_10_pages - num_photos_next_10_pages

    # Calculate the number of photos to be placed on each of the remaining pages
    num_photos_per_page = remaining_photos / (num_pages - 20)
    result = int(num_photos_per_page)
    return result

print(solution())