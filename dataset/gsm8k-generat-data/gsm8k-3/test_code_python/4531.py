def solution():
    """In a newspaper, each one of 12 pages holds 2 photos and each of another 9 pages hold 3 photos. How many photos are used in the newspaper?"""
    # Define the number of pages and photos per page
    PAGE_2_PHOTOS = 2
    PAGE_3_PHOTOS = 3
    PAGE_12_NUM = 12
    PAGE_9_NUM = 9

    # Calculate the total number of photos on the 12 pages
    page_2_photos = PAGE_2_PHOTOS * PAGE_12_NUM

    # Calculate the total number of photos on the 9 pages
    page_3_photos = PAGE_3_PHOTOS * PAGE_9_NUM

    # Calculate the total number of photos in the newspaper
    total_photos = page_2_photos + page_3_photos

    # Display the total number of photos
    result = total_photos
    return result

print(solution())