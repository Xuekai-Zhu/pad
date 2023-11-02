def solution():
    mike_books_tuesday = 45
    corey_books_tuesday = mike_books_tuesday * 2
    mike_books_wednesday = mike_books_tuesday - 10
    corey_books_wednesday = corey_books_tuesday - 15

    # Calculate total number of books given to Lily
    total_books_given = (mike_books_wednesday - mike_books_tuesday) + (corey_books_wednesday - corey_books_tuesday)

    result = total_books_given
    return result

print(solution())