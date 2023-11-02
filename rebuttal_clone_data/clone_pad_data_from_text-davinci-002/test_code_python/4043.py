def solution():
    puzzle1 = 1000
    puzzle2 = puzzle1 + (puzzle1 * 0.5)
    puzzle3 = puzzle2 + (puzzle2 * 0.5)
    total_pieces = puzzle1 + puzzle2 + puzzle3
    result = total_pieces
    return result

print(solution())