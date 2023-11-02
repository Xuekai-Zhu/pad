def solution():
    """Bert fills out the daily crossword puzzle in the newspaper every day. He uses up a pencil to fill out the puzzles every two weeks. On average, it takes him 1050 words to use up a pencil. How many words are in each crossword puzzle on average?"""
    # Calculate the number of words Bert uses per day
    words_per_day = 1050 / 14

    # Calculate the number of words per crossword puzzle on average
    words_per_puzzle = words_per_day / 7

    # Display the average number of words per crossword puzzle
    result = words_per_puzzle
    return result

print(solution())