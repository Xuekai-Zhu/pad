def solution():
     """John writes 20 pages a day. How long will it take him to write 3 books that are 400 pages each?"""
    days_to_write_one_book = 400 / 20
    days_to_write_three_books = days_to_write_one_book * 3
    result = days_to_write_three_books
    return result

print(solution())