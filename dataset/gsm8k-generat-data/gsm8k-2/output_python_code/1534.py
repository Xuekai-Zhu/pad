def solution():
    """Janine read 5 books last month. This month, she read twice as many books. If each book has 10 pages, how many pages did Janine read in two months?"""
    last_month_books = 5
    this_month_books = last_month_books * 2
    book_pages = 10
    total_pages = (last_month_books + this_month_books) * book_pages
    result = total_pages
    return result

print(solution())