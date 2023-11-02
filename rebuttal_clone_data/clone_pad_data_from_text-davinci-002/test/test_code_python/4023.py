def solution():
    average_pieces_per_hour = 100
    hours_per_day = 7
    puzzles_300 = 8
    pieces_300 = 300
    puzzles_500 = 5
    pieces_500 = 500
    total_pieces = (puzzles_300 * pieces_300) + (puzzles_500 * pieces_500)
    total_hours = total_pieces / average_pieces_per_hour
    total_days = total_hours / hours_per_day
    result = total_days
    return result

print(solution())