def solution():
    """Luke started working on a 1000-piece jigsaw puzzle. The first day he worked on it, he put together 10% of the pieces.
    On the second day, he put together another 20% of the remaining pieces from the first day.
    On the third day, he put together 30% of the remaining pieces from the previous day.
    How many pieces does he have left to complete after the third day?"""
    total_pieces = 1000
    first_day_pieces = total_pieces * 0.1
    remaining_pieces = total_pieces - first_day_pieces
    second_day_pieces = remaining_pieces * 0.2
    remaining_pieces = remaining_pieces - second_day_pieces
    third_day_pieces = remaining_pieces * 0.3
    pieces_left = remaining_pieces - third_day_pieces
    result = pieces_left
    return result

print(solution())