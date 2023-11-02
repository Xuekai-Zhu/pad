def solution():
    """Xander read 20% of his 500-page book in one hour. The next night he read another 20% of the book. On the third night, he read 30% of his book. How many pages does he have left to read?"""
    book_pages = 500
    first_night = book_pages * 0.2
    second_night = book_pages * 0.2
    third_night = book_pages * 0.3
    pages_left = book_pages - (first_night + second_night + third_night)
    result = pages_left
    return result

print(solution())