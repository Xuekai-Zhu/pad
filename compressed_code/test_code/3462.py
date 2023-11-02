def solution():
    
    book_weight = 0.5
    textbook_weight = 2
    knick_knack_weight = 6
    max_weight = 80
    total_weight = (70 * book_weight) + (30 * textbook_weight) + (3 * knick_knack_weight)
    excess_weight = total_weight - max_weight
    result = excess_weight
    return result

print(solution())