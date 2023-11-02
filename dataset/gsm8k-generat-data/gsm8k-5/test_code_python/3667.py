def solution():
    book_pages = 100  # The book has 100 pages
    pages_read_so_far = 15 + 2*15 + (2*15+5)  # Juwella read 15 pages three nights ago, twice that two nights ago, and 5 more than the previous night last night
    pages_remaining = book_pages - pages_read_so_far  # Juwella needs to read the remaining pages

    result = pages_remaining
    return result

print(solution())