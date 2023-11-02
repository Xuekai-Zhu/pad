def solution():
    num_books_10 = 4
    num_books_15 = 6
    stamps_per_book_10 = 10
    stamps_per_book_15 = 15

    # Calculate the total number of stamps from the books with 10 stamps per book
    total_stamps_10 = num_books_10 * stamps_per_book_10

    # Calculate the total number of stamps from the books with 15 stamps per book
    total_stamps_15 = num_books_15 * stamps_per_book_15

    # Calculate the total number of stamps that Ruel has
    total_stamps = total_stamps_10 + total_stamps_15
    result = total_stamps
    return result

print(solution())