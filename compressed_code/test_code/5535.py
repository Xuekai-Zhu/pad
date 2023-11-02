def solution():
    
    puzzle_1_size = 300
    puzzle_2_size = 500
    puzzle_1_count = 8
    puzzle_2_count = 5
    pieces_per_hour = 100
    max_hours_per_day = 7

    total_puzzle_pieces = (puzzle_1_size * puzzle_1_count) + (puzzle_2_size * puzzle_2_count)
    total_hours = total_puzzle_pieces / pieces_per_hour
    total_days = total_hours / max_hours_per_day
    result = total_days
    return result

print(solution())