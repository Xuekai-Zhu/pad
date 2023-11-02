def solution():
    
    puzzle_size = 2000
    pieces_completed_per_10_minutes = 100
    time_per_10_minutes = 10
    total_pieces = puzzle_size * 2
    total_time_in_minutes = (total_pieces / pieces_completed_per_10_minutes) * time_per_10_minutes
    result = total_time_in_minutes
    return result

print(solution())