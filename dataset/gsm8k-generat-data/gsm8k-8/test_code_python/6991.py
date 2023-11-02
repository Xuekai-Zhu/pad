def solution():
    total_pieces = 1000
    first_day_pieces = total_pieces * 0.1
    remaining_pieces = total_pieces - first_day_pieces
    second_day_pieces = remaining_pieces * 0.2
    remaining_pieces -= second_day_pieces
    third_day_pieces = remaining_pieces * 0.3
    remaining_pieces -= third_day_pieces
    result = remaining_pieces
    return result

print(solution())