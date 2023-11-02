def solution():
    # Calculate the total number of new books Brianna will have
    new_books = 6 + 8 + (8 - 2)

    # Calculate the total number of books Brianna will read this year
    total_books = new_books + 24  # 2 books a month for 12 months

    # Determine how many old books Brianna will need to reread to have 2 books to read each month
    old_books_to_reread = total_books - 24  # Subtracting the 24 books she will read that are not old

    # Determine how many old books Brianna had to begin with
    old_books_total = old_books_to_reread + 24  # Adding back in the 24 old books she will read without rereading

    result = old_books_to_reread
    return result

print(solution())