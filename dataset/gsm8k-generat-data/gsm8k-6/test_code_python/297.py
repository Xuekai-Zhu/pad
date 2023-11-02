def solution():
    # Calculate the average number of words in each crossword puzzle
    words_per_pencil = 1050  # number of words Bert can write with one pencil
    weeks_per_pencil = 2  # number of weeks it takes Bert to use up one pencil
    puzzles_per_week = 7  # number of crossword puzzles Bert fills out each week
    words_per_puzzle = words_per_pencil / (weeks_per_pencil * puzzles_per_week)  # average number of words in each puzzle
    result = words_per_puzzle
    return result

print(solution())