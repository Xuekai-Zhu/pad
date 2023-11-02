def solution():
    total_length = 30
    number_of_pieces = 6
    pieces_used = 4
    pieces_not_used = number_of_pieces - pieces_used
    length_of_each_piece = total_length / number_of_pieces
    meters_not_used = pieces_not_used * length_of_each_piece
    result = meters_not_used
    
    return result

print(solution())