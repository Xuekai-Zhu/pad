def solution():
    max_weight = 80
    hardcover_books = 70
    book_weight = 0.5
    textbooks = 30
    textbook_weight = 2
    knickknacks = 3
    knickknack_weight = 6
    total_weight = (hardcover_books * book_weight) + (textbooks * textbook_weight) + (knickknacks * knickknack_weight)
    weight_over_limit = total_weight - max_weight
    result = weight_over_limit
    
    return result

print(solution())