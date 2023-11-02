def solution():
    
    weight_limit = 80
    book_weight = 0.5
    hardcover_books = 70
    textbook_weight = 2
    textbooks = 30
    knick_knack_weight = 6
    knick_knacks = 3
    total_weight = (book_weight * hardcover_books) + (textbook_weight * textbooks) + (knick_knack_weight * knick_knacks)
    weight_over_limit = total_weight - weight_limit
    result = weight_over_limit
    return result

print(solution())