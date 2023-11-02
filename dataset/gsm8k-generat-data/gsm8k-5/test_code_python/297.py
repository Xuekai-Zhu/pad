def solution():
    pencils_per_two_weeks = 1  # Bert uses up one pencil every two weeks
    words_per_pencil = 1050  # It takes Bert 1050 words to use up a pencil

    # Calculate the number of words per crossword puzzle on average
    words_per_puzzle = words_per_pencil / pencils_per_two_weeks / 14  # Divide by 14 to get the number of words per puzzle

    result = words_per_puzzle
    return result

print(solution())