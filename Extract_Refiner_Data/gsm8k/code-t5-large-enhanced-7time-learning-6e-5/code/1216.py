def solution():
    
    # Define the length of the board and the ratio of longer to shorter piece
    board_length = 40
    ratio = 4

    # Calculate the length of the shorter piece
    shorter_piece = board_length / (1 + ratio)

    # Calculate the length of the longer piece
    longer_piece = ratio * shorter_piece

    # Display the length of the longer piece
    result = longer_piece
    return result

print(solution())