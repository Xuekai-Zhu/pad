def solution():
    # Total number of pages in each book
    book1_pages = 20
    book2_pages = 12
    # Nico read book 3, so we don't know how many pages it has

    # Total pages Nico read from Monday to Wednesday
    total_pages_read = 51

    # Nico read book 1 on Monday, so subtract its pages from the total
    total_pages_read -= book1_pages

    # Nico read book 2 on Tuesday, so subtract its pages from the remaining total
    total_pages_read -= book2_pages

    # Calculate the number of pages Nico read on Wednesday (book 3)
    pages_read_on_wednesday = total_pages_read

    return pages_read_on_wednesday

print(solution())