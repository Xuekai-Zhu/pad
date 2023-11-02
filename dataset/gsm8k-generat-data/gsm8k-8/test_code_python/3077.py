def solution():
    # Calculate the number of books donated by 10 people, each donating 5 books
    donated_books = 10 * 5

    # Calculate the total number of books in the store
    total_books = 300 + donated_books

    # Calculate the number of books returned after being borrowed
    returned_books = 140

    # Calculate the number of books remaining in the store
    remaining_books = total_books - returned_books

    result = remaining_books
    return result

print(solution())