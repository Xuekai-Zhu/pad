def solution():
    total_pieces = 300  # Mrs. Young bought a 300 piece puzzle set
    num_sons = 3  # Mrs. Young has three sons

    # Divide the puzzle pieces evenly among the sons
    pieces_per_son = total_pieces / num_sons

    # Calculate the number of pieces placed by each son
    pieces_placed_reyn = 25
    pieces_placed_rhys = 2 * pieces_placed_reyn
    pieces_placed_rory = 3 * pieces_placed_reyn

    # Calculate the total number of pieces placed
    total_pieces_placed = pieces_placed_reyn + pieces_placed_rhys + pieces_placed_rory

    # Calculate the number of pieces left to be placed
    pieces_left = total_pieces - total_pieces_placed
    result = pieces_left
    return result

print(solution())