def solution():
    """Jade is building a lego tower. She has 100 pieces. Each level has to be 7 pieces wide. If she has 23 pieces left at the end, how many levels is her tower?"""
    total_pieces = 100
    pieces_per_level = 7
    leftover_pieces = 23
    used_pieces = total_pieces - leftover_pieces
    levels = used_pieces // pieces_per_level
    result = levels
    return result

print(solution())