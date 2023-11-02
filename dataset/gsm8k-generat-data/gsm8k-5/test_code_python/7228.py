def solution():
    matt_books_year1 = x  # Let's assume Matt read x books in his first year
    pete_books_year1 = 2*x  # Pete read twice the number of books Matt did in his first year
    pete_books_year2 = 2*pete_books_year1  # Pete doubled his number of books from the previous year
    matt_books_year2 = 1.5*75  # Matt read 50% more books than last year, which was 75 books

    total_books = matt_books_year1 + pete_books_year1 + matt_books_year2 + pete_books_year2
    result = total_books
    return result

print(solution())