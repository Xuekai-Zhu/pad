def solution():
    cake_pieces = 240
    cake_eaten = 60
    cake_remaining = cake_pieces - cake_eaten
    cake_pieces_sister = cake_remaining / 3
    result = cake_pieces_sister
    return result

print(solution())