def solution():
    """Maya loves to read books. Last week she read 5 books. Each book had 300 pages of text. This week she read twice as much. How many pages did Maya read in total?"""
    books_last_week = 5
    pages_per_book = 300
    books_this_week = books_last_week * 2
    pages_this_week = books_this_week * pages_per_book
    total_pages = (books_last_week * pages_per_book) + pages_this_week
    result = total_pages
    return result

print(solution())