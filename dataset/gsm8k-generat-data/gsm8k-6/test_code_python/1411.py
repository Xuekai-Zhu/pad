def solution():
    # Calculate the total number of words already written by Leo
    words_written = 20 * 10 * 1.5  # 20 lines per page, 10 words per line, 1.5 pages filled

    # Calculate the number of words left to write
    words_left = 400 - words_written
    result = words_left
    return result

print(solution())