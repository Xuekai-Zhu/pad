def solution():
    words_per_day = 1050
    days_per_week = 7
    puzzles_per_week = 1
    words_per_puzzle = words_per_day / (days_per_week * puzzles_per_week)
    result = words_per_puzzle
    return result

print(solution())