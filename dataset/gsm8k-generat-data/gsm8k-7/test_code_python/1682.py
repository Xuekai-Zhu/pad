def solution():
    books_per_year = 6  # John writes a book every 2 months, so he writes 6 books per year
    years_writing = 20
    avg_income_per_book = 30000

    # Calculate the total number of books John has written
    total_books_written = books_per_year * years_writing

    # Calculate John's total earnings from writing
    total_earnings = total_books_written * avg_income_per_book
    result = total_earnings
    return result

print(solution())