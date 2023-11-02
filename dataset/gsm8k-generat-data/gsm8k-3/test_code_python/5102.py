def solution():
    """Loris needs three more books to have the same number as Lamont, who has twice the number of books Darryl has. If Darryl has 20 books, calculate the total number of books the three have."""
    # Define Darryl's number of books
    darryl_books = 20

    # Calculate Lamont's number of books
    lamont_books = darryl_books * 2

    # Calculate Loris's number of books
    loris_books = lamont_books - 3

    # Calculate the total number of books the three have
    total_books = darryl_books + lamont_books + loris_books

    # Display the total number of books
    result = total_books
    return result

print(solution())