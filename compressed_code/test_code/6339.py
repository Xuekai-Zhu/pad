def solution():
    
    book_length = 600
    first_week = book_length / 2
    remaining_pages = book_length - first_week
    second_week = remaining_pages * 0.3
    third_week = book_length - first_week - second_week
    result = third_week
    return result

print(solution())