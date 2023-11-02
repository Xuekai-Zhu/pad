def solution():
    # Calculate the number of pieces each son receives
    pieces_per_son = 300 / 3 

    # Calculate the number of pieces placed by each son
    pieces_placed_reyn = 25
    pieces_placed_rhys = 2 * pieces_placed_reyn
    pieces_placed_rory = 3 * pieces_placed_reyn

    # Calculate the total number of pieces placed
    total_pieces_placed = pieces_placed_reyn + pieces_placed_rhys + pieces_placed_rory
    
    # Calculate the number of pieces still left to be placed
    pieces_left = 300 - total_pieces_placed
    result = pieces_left
    return result

print(solution())