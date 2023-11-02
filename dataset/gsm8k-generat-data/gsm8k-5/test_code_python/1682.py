def solution():
    books_per_year = 6  # John writes a book every 2 months, so he writes 6 books per year
    years_writing = 20
    average_income = 30000  # John earns an average of $30,000 per book

    # Calculate the total number of books John has written over 20 years
    total_books = books_per_year * years_writing

    # Calculate the total amount of money John has made writing
    total_income = total_books * average_income
    result = total_income
    return result

print(solution())