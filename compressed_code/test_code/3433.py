def solution():
    
    puzzle_pieces = 300
    num_sons = 3
    pieces_per_son = puzzle_pieces // num_sons
    reyn_pieces = 25
    rhys_pieces = 2 * reyn_pieces
    rory_pieces = 3 * reyn_pieces
    total_pieces_placed = reyn_pieces + rhys_pieces + rory_pieces
    pieces_left = puzzle_pieces - total_pieces_placed
    result = pieces_left
    return result

print(solution())