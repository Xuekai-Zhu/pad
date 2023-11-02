def solution():
    # Calculate the number of broken pieces that Anne didn't sweep up
    remaining_pieces = 60 / 2  # Anne sweeps up half of the pieces, leaving 30 remaining
    remaining_pieces -= 3  # Her cat steals 3 pieces, leaving 27 remaining
    pieces_picked_up = remaining_pieces / 3  # Her boyfriend picks up 1/3 of the remaining pieces
    result = pieces_picked_up
    return result

print(solution())