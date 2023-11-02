def solution():
    """Jason bought a new bookcase that can hold a maximum of 80 pounds of weight. Jason has 70 hardcover books that each weigh half a pound, 30 textbooks that each weigh 2 pounds, and 3 knick-knacks that each weight 6 pounds. How many pounds over the bookcase's weight limit is this total collection of items?"""
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