def solution():
    
    pencils_per_week = 1 / 2
    words_per_pencil = 1050
    total_puzzles_per_week = 7
    words_per_puzzle = (pencils_per_week * words_per_pencil) / total_puzzles_per_week
    result = words_per_puzzle
    return result

print(solution())