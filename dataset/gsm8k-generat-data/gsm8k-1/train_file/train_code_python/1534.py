def solution():
    """Janine read 5 books last month. This month, she read twice as many books. If each book has 10 pages, how many pages did Janine read in two months?"""
    books_last_month = 5
    books_this_month = books_last_month * 2
    pages_per_book = 10
    total_pages = (books_last_month + books_this_month) * pages_per_book
    result = total_pages
    return result

print(solution())