def solution():
    """Anne drops a mirror and breaks it into 60 pieces. She sweeps up half of them, then her cat steals 3 pieces and her boyfriend picks up 1/3 of the remaining pieces. How many pieces does her boyfriend pick up?"""
    total_pieces = 60
    swept_pieces = total_pieces / 2
    stolen_pieces = 3
    remaining_pieces = total_pieces - swept_pieces - stolen_pieces
    boyfriend_pieces = remaining_pieces / 3
    result = boyfriend_pieces
    return result

print(solution())