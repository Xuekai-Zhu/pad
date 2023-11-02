def solution():
    """Leo has to write a 400-word story for his literature class. 10 words fit on each line of his notebook and 20 lines fit on each page. Lucas has filled one and a half pages. How many words does he have left to write?"""
    # Define the number of lines filled
    lines_filled = 1.5 * 20

    # Define the number of words per line
    words_per_line = 10

    # Calculate the total number of words written so far
    words_written = lines_filled * words_per_line

    # Calculate the number of words left to write
    words_left = 400 - words_written

    # Display the number of words left to write
    result = words_left
    return result

print(solution())