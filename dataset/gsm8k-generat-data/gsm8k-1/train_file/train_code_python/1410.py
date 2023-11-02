def solution():
    """Leo has to write a 400-word story for his literature class. 10 words fit on each line of his notebook and 20 lines fit on each page. Lucas has filled one and a half pages. How many words does he have left to write?"""
    words_per_line = 10
    lines_per_page = 20
    pages_filled = 1.5
    words_filled = words_per_line * lines_per_page * pages_filled
    words_left = 400 - words_filled
    result = words_left
    return result

print(solution())