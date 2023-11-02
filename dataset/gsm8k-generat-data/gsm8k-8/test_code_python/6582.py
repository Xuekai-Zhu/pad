def solution():
    # Define the number of pages in the new edition Geometry book
    new_geometry_pages = 450

    # Calculate twice as many pages as the new edition
    twice_new_pages = 2 * new_geometry_pages

    # Calculate the number of pages in the old edition
    old_geometry_pages = twice_new_pages + 230
    result = old_geometry_pages
    return result

print(solution())