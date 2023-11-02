def solution():
    total_pieces = 60  # Anne breaks the mirror into 60 pieces
    swept_pieces = total_pieces / 2  # Anne sweeps up half of the pieces
    remaining_pieces = total_pieces - swept_pieces  # Anne has this many pieces left

    # Her cat steals 3 pieces, so the remaining pieces are decreased by 3
    remaining_pieces -= 3

    # Her boyfriend picks up 1/3 of the remaining pieces
    boyfriend_pieces = remaining_pieces / 3
    result = boyfriend_pieces
    return result

print(solution())