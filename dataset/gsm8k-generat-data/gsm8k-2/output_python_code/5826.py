def solution():
    """Yesterday Ryan got five books from the library. They were a total of 2100 pages. His brother got one book a day that was 200 pages each. They both finished them in a week. On average, how many more pages per day did Ryan read compared to his brother?"""
    ryan_total_pages = 2100
    ryan_total_books = 5
    ryan_pages_per_book = ryan_total_pages / ryan_total_books
    ryan_pages_per_day = ryan_pages_per_book / 7

    brother_total_books = 7
    brother_pages_per_book = 200
    brother_total_pages = brother_total_books * brother_pages_per_book
    brother_pages_per_day = brother_total_pages / 7

    difference_pages_per_day = ryan_pages_per_day - brother_pages_per_day
    result = difference_pages_per_day
    return result

print(solution())