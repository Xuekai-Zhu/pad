def solution():
    max_weight = 80
    num_hardcover_books = 70
    hardcover_book_weight = 0.5
    num_textbooks = 30
    textbook_weight = 2
    num_knickknacks = 3
    knickknack_weight = 6

    # Calculate the total weight of all hardcover books
    total_hardcover_weight = num_hardcover_books * hardcover_book_weight

    # Calculate the total weight of all textbooks
    total_textbook_weight = num_textbooks * textbook_weight

    # Calculate the total weight of all knick-knacks
    total_knickknack_weight = num_knickknacks * knickknack_weight

    # Calculate the total weight of the entire collection of items
    total_weight = total_hardcover_weight + total_textbook_weight + total_knickknack_weight

    # Calculate the weight over the bookcase's weight limit
    weight_over_limit = total_weight - max_weight

    result = weight_over_limit
    return result

print(solution())