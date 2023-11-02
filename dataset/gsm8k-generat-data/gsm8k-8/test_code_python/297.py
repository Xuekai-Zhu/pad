def solution():
    # Define the variables
    pencils_per_week = 1/2
    words_per_pencil = 1050

    # Calculate the average words per crossword puzzle
    week_words = pencils_per_week * words_per_pencil
    average_words_per_puzzle = week_words / 7
    result = average_words_per_puzzle
    return result

print(solution())