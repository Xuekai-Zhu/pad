def solution():
    total_books = 14  # The Rangers Apprentice series has 14 books
    pages_per_book = 200  # Each book has 200 pages
    books_read_first_month = 4  # Sabrina read 4 books in the first month
    books_remaining = total_books - books_read_first_month  # Sabrina has some books remaining to be read

    # Sabrina reads half of the remaining books in the second month
    books_read_second_month = books_remaining / 2

    # Calculate the total number of pages Sabrina needs to read to finish the series
    total_pages = (books_read_first_month + books_read_second_month) * pages_per_book
    result = total_pages
    return result

print(solution())