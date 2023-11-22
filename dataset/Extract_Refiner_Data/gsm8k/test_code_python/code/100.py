def solution():
    
    # Define the total number of jigsaw pieces
    total_pieces = 1000

    # Calculate the number of pieces placed on the board
    board_pieces = total_pieces / 4

    # Calculate the number of pieces remaining after the board
    remaining_pieces = total_pieces - board_pieces

    # Calculate the number of pieces placed by her mom
    mom_pieces = remaining_pieces / 3

    # Calculate the number of pieces left to be placed
    pieces_left = remaining_pieces - mom_pieces

    # Display the number of pieces left to be placed
    result = pieces_left
    return result

print(solution())