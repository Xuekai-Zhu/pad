def solution():
    num_history_books = 12
    num_fiction_books = 19
    num_children_books = 8

    # Add the 4 misplaced children's books to the total number of children's books
    num_children_books += 4

    # Subtract the number of books already shelved from the total number of books in the cart
    remaining_books = 16
    total_books = remaining_books + num_history_books + num_fiction_books + num_children_books

    result = total_books
    return result

print(solution())