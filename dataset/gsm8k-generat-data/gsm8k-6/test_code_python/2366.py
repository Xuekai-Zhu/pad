def solution():
    # Calculate the total number of photos placed on the first 20 pages
    photos_on_first_20 = 3*10 + 4*10  # 3 photos each on first 10 pages and 4 photos each on next 10 pages
    photos_remaining = 100 - photos_on_first_20  # number of photos remaining to be placed
    pages_remaining = 30 - 20  # number of pages remaining
    photos_per_page = photos_remaining // pages_remaining  # integer division to find the number of photos per remaining page
    result = photos_per_page
    return result

print(solution())