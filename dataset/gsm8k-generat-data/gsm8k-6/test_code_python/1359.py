def solution():
    # Calculate the number of pages Lucy can read in 1 hour
    lucy_pages = 40 + 20  # Lucy can read 20 more pages than Oliver who can read 40 pages
    # Calculate the number of pages Carter can read in 1 hour
    carter_pages = lucy_pages / 2  # Carter can read half as many pages as Lucy
    result = carter_pages
    return result

print(solution())