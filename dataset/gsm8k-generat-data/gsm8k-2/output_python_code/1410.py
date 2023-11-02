def solution():
    """Leo has to write a 400-word story for his literature class. 10 words fit on each line of his notebook and 20 lines fit on each page. Lucas has filled one and a half pages. How many words does he have left to write?"""
    total_lines = 1.5 * 20
    remaining_lines = 20 - (total_lines % 20)
    remaining_words = remaining_lines * 10
    words_left = 400 - remaining_words
    result = words_left
    return result

print(solution())