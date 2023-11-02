def solution():
    """Loris needs three more books to have the same number as Lamont, who has twice the number of books Darryl has. If Darryl has 20 books, calculate the total number of books the three have."""
    
    # Define the number of books Darryl has
    darryl_books = 20

    # Calculate the number of books Lamont has, which is twice the number of Darryl's books
    lamont_books = 2 * darryl_books

    # Calculate the number of books Loris has, which is three less than Lamont's books
    loris_books = lamont_books - 3

    # Calculate the total number of books they have together
    total_books = darryl_books + lamont_books + loris_books

    # Return the result
    result = total_books
    return result

print(solution())