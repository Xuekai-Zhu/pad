def solution():
    """Jason bought a new bookcase that can hold a maximum of 80 pounds of weight. Jason has 70 hardcover books that each weigh half a pound, 30 textbooks that each weigh 2 pounds, and 3 knick-knacks that each weight 6 pounds. How many pounds over the bookcase's weight limit is this total collection of items?"""
    book_weight = 0.5
    textbook_weight = 2
    knick_knack_weight = 6
    max_weight = 80
    total_weight = (70 * book_weight) + (30 * textbook_weight) + (3 * knick_knack_weight)
    excess_weight = total_weight - max_weight
    result = excess_weight
    return result

print(solution())