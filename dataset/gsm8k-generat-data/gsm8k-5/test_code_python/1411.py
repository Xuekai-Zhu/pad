def solution():
    words_per_line = 10  # 10 words fit on each line of Leo's notebook
    lines_per_page = 20  # 20 lines fit on each page
    total_pages = 1.5  # Leo has already filled 1.5 pages

    # Calculate the total words written so far
    words_written = words_per_line * lines_per_page * total_pages

    # Calculate the words left to write
    words_left = 400 - words_written
    result = words_left
    return result

print(solution())