def solution():
    """Bert fills out the daily crossword puzzle in the newspaper every day. He uses up a pencil to fill out the puzzles every two weeks. On average, it takes him 1050 words to use up a pencil. How many words are in each crossword puzzle on average?"""
    words_per_pencil = 1050
    puzzles_per_week = 7 * 2  # crossword puzzle every day for two weeks
    words_per_puzzle = words_per_pencil / puzzles_per_week
    result = words_per_puzzle
    return result

print(solution())