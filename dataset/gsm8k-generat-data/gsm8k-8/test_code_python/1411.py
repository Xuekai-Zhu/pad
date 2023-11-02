def solution():
    # Calculate the total number of lines filled by Leo
    total_lines = 1.5 * 20

    # Calculate the total number of words used
    total_words_used = total_lines * 10

    # Calculate the number of words left to write
    words_left_to_write = 400 - total_words_used

    result = words_left_to_write
    return result

print(solution())