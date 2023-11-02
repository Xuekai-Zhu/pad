def solution():
    num_books = 100
    num_people = 5
    books_per_person = 2
    additional_books = 20

    # Calculate the total number of books borrowed on the first day
    num_books_borrowed = num_people * books_per_person

    # Subtract the number of books borrowed on the first day from the total number of books
    num_books -= num_books_borrowed

    # Add the number of additional books borrowed on the second day
    num_books += additional_books

    result = num_books
    return result

print(solution())