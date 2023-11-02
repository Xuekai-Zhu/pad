def solution():
    # Calculate the number of regular letters Steve writes in a month
    regular_letters = 30 / 3  # Steve writes a letter every 3rd day
    regular_time = regular_letters * 20  # Each regular letter takes 20 minutes
    regular_pages = regular_time / 10  # Each page takes 10 minutes to write

    # Calculate the number of pages in the long letter
    long_time = 80  # Steve spends 80 minutes on the long letter
    long_pages = (long_time / 2) / 10  # The long letter takes twice as long per page

    # Calculate the total number of pages Steve writes in a month
    total_pages = regular_pages + long_pages
    result = total_pages
    return result

print(solution())