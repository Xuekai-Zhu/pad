def solution():
    """Jerry has an interesting novel he borrowed from a friend to read over the weekend. The book has 93 pages. On Saturday, he reads 30 pages. On Sunday, he goes to church and comes back, sits down, and reads 20 pages of the book. How many pages are remaining before Jerry can finish the book?"""
    total_pages = 93
    saturday_pages = 30
    sunday_pages = 20
    remaining_pages = total_pages - saturday_pages - sunday_pages
    result = remaining_pages
    return result

print(solution())