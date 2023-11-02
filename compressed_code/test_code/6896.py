def solution():
    
    words_per_line = 10
    lines_per_page = 20
    pages_filled = 1.5
    words_filled = words_per_line * lines_per_page * pages_filled
    words_left = 400 - words_filled
    result = words_left
    return result

print(solution())