def solution():
    """Tobias bought a big pizza with 60 pieces. He ate 2/5 of the pieces on the first day,
    10 pieces on the second day, and 7/13 of the remaining pieces on the third day. 
    How many pizza pieces has he eaten so far?"""
    total_pieces = 60
    first_day_pieces = (2/5) * total_pieces
    remaining_pieces = total_pieces - first_day_pieces
    second_day_pieces = 10
    third_day_pieces = (7/13) * remaining_pieces
    total_pieces_eaten = first_day_pieces + second_day_pieces + third_day_pieces
    result = total_pieces_eaten
    return result

print(solution())