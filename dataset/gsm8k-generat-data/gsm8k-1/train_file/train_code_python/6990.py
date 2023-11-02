def solution():
    """Luke started working on a 1000-piece jigsaw puzzle. The first day he worked on it, he put together 10% of the pieces. On the second day, he put together another 20% of the remaining pieces from the first day. On the third day, he put together 30% of the remaining pieces from the previous day. How many pieces does he have left to complete after the third day?"""
    total_pieces = 1000
    day_1 = total_pieces * 0.1
    remaining_pieces_1 = total_pieces - day_1
    day_2 = remaining_pieces_1 * 0.2
    remaining_pieces_2 = remaining_pieces_1 - day_2
    day_3 = remaining_pieces_2 * 0.3
    remaining_pieces_3 = remaining_pieces_2 - day_3
    result = remaining_pieces_3
    return result

print(solution())