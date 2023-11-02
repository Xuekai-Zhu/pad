def solution():
    # Calculate the number of pages remaining after the first week
    pages_remaining = 500 - 150

    # Calculate the number of pages written on in the second week
    pages_written = 0.3 * pages_remaining

    # Calculate the number of damaged empty pages
    damaged_pages = 0.2 * (500 - pages_remaining - pages_written)

    # Calculate the total number of empty pages remaining
    empty_pages = pages_remaining - pages_written - damaged_pages

    result = empty_pages
    return result

print(solution())