def solution():
    """Jerry has an interesting novel he borrowed from a friend to read over the weekend. The book has 93 pages. On Saturday, he reads 30 pages. On Sunday, he goes to church and comes back, sits down, and reads 20 pages of the book. How many pages are remaining before Jerry can finish the book?"""
    total_pages = 93
    pages_read_saturday = 30
    pages_read_sunday = 20
    pages_remaining = total_pages - pages_read_saturday - pages_read_sunday
    result = pages_remaining
    return result

print(solution())