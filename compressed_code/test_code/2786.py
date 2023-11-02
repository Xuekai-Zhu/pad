def solution():
    
    book_length = 354
    day_1 = 63
    day_2 = day_1 * 2
    day_3 = day_2 + 10
    total_first_three_days = day_1 + day_2 + day_3
    day_4 = book_length - total_first_three_days
    result = day_4
    return result

print(solution())