def solution():
    # Define the weight of each type of book
    math_book_weight = 2
    english_book_weight = 4
    history_book_weight = 2 * english_book_weight

    # Calculate the total weight of all the books
    total_weight = math_book_weight + english_book_weight + history_book_weight
    result = total_weight
    return result

print(solution())