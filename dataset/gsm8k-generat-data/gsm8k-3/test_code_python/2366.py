def solution():
    """Alyssa took 100 photos on vacation. She wants to put them in a photo album with 30 pages. She can place 3 photos each on the first 10 pages. Then she can place 4 photos each on the next 10 pages. If she wants to put an equal number of photos on each of the remaining pages of the album, how many photos can she place on each page?"""
    # Calculate the number of photos used in the first 20 pages
    photos_used_first_20 = 3 * 10 + 4 * 10

    # Calculate the number of pages remaining
    pages_remaining = 30 - 20

    # Calculate the number of photos remaining
    photos_remaining = 100 - photos_used_first_20

    # Calculate the number of photos she can place on each of the remaining pages
    photos_per_page = photos_remaining // pages_remaining

    # Display the number of photos she can place on each of the remaining pages
    result = photos_per_page
    return result

print(solution())