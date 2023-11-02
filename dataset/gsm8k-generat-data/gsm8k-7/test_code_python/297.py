def solution():
    pencils_per_weeks = 1/2
    words_per_pencil = 1050
    puzzles_per_week = 7
    pencils_per_puzzle = pencils_per_weeks/puzzles_per_week
    words_per_puzzle = words_per_pencil*pencils_per_puzzle
    result = words_per_puzzle
    return result

print(solution())