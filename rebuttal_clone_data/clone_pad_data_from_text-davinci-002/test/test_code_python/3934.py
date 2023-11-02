def solution():
    pieces_available = 100
    pieces_per_level = 7
    pieces_left_over = 23
    total_levels = (pieces_available - pieces_left_over) / pieces_per_level
    result = total_levels
    return result

print(solution())