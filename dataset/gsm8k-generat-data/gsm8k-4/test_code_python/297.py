def solution():
    """Bert fills out the daily crossword puzzle in the newspaper every day. He uses up a pencil to fill out the puzzles every two weeks. On average, it takes him 1050 words to use up a pencil. How many words are in each crossword puzzle on average?"""
    # Define the number of words Bert can write with a single pencil
    words_per_pencil = 1050

    # Define the number of weeks it takes Bert to finish a pencil
    weeks_per_pencil = 2

    # Calculate the number of words Bert writes in one week
    words_per_week = words_per_pencil / weeks_per_pencil

    # Calculate the number of words in each crossword puzzle
    puzzles_per_week = 7
    words_per_puzzle = words_per_week / puzzles_per_week

    # Return the result
    result = words_per_puzzle
    return result

print(solution())