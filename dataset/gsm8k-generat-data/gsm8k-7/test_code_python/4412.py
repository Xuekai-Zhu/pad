def solution():
    puzzle_pieces = 300
    num_sons = 3
    reyn_pieces = 25
    rhys_pieces = 2 * reyn_pieces
    rory_pieces = 3 * reyn_pieces

    # Calculate the total number of pieces placed by all three sons
    total_pieces_placed = (reyn_pieces + rhys_pieces + rory_pieces) * num_sons

    # Calculate the number of pieces remaining
    remaining_pieces = puzzle_pieces - total_pieces_placed
    result = remaining_pieces
    return result

print(solution())