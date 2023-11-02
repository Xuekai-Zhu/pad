def solution():
    words_per_line = 10
    lines_per_page = 20
    total_pages_filled = 1.5
    total_words_filled = words_per_line * lines_per_page * total_pages_filled
    total_words_needed = 400
    words_left_to_write = total_words_needed - total_words_filled
    result = words_left_to_write
    return result

print(solution())