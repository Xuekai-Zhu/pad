def solution():
    """Loris needs three more books to have the same number as Lamont, who has twice the number of books Darryl has. If Darryl has 20 books, calculate the total number of books the three have."""
    darryl_books = 20
    lamont_books = 2 * darryl_books
    loris_books = lamont_books - 3
    total_books = darryl_books + lamont_books + loris_books
    result = total_books
    return result

print(solution())