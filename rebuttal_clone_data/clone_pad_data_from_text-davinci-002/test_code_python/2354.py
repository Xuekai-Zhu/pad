def solution():
    starting_number_of_books = 100
    books_borrowed_on_first_day = 10
    books_borrowed_on_second_day = 20
    total_books_borrowed = books_borrowed_on_first_day + books_borrowed_on_second_day
    remaining_books = starting_number_of_books - total_books_borrowed
    result = remaining_books
    return result

print(solution())