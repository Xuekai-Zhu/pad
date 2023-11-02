def solution():
    # Define the variables
    total_pieces = 300
    num_of_sons = 3
    reyn_pieces = 25
    rhys_pieces = 2 * reyn_pieces
    rory_pieces = 3 * reyn_pieces

    # Calculate the total number of pieces placed
    total_placed = reyn_pieces + rhys_pieces + rory_pieces

    # Calculate the number of pieces left
    pieces_left = total_pieces - total_placed

    result = pieces_left
    return result

print(solution())