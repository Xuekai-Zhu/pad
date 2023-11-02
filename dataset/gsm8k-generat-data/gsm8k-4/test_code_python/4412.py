def solution():
    """Mrs. Young buys a 300 piece puzzle set for her three sons.  She divides the pieces evenly to the three boys.  Reyn can place 25 pieces into the puzzle picture.  Rhys places twice as much as Reyn.  Rory places three times as much as Reyn. Altogether, how many puzzle pieces are still left to be placed?"""
    # Define the total number of puzzle pieces
    total_puzzle_pieces = 300

    # Divide the pieces evenly among the three boys
    pieces_per_boy = total_puzzle_pieces // 3

    # Calculate the number of pieces placed by each boy
    reyn_pieces = 25
    rhys_pieces = 2 * reyn_pieces
    rory_pieces = 3 * reyn_pieces

    # Calculate the total number of placed pieces
    total_placed_pieces = reyn_pieces + rhys_pieces + rory_pieces

    # Calculate the number of pieces still left to be placed
    pieces_left = total_puzzle_pieces - total_placed_pieces

    # return the result
    result = pieces_left
    return result

print(solution())