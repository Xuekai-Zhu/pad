def solution():
    mike_books_tuesday = 45
    corey_books_tuesday = 2 * mike_books_tuesday

    mike_books_wednesday = mike_books_tuesday - 10
    corey_books_wednesday = corey_books_tuesday - 15

    lily_books_wednesday = mike_books_wednesday + corey_books_wednesday - (mike_books_tuesday + corey_books_tuesday)

    result = lily_books_wednesday
    return result

print(solution())