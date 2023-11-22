def solution():
    
    # Define the initial number of candy pieces
    candy_pieces = 100

    # Define the number of candy pieces eaten by Ginger and Amy per day
    ginger_pieces = 4 * 7
    amy_pieces = 3 * 7

    # Calculate the number of candy pieces left after two weeks
    candy_pieces_left = candy_pieces - ginger_pieces - amy_pieces

    # return the result
    result = candy_pieces_left
    return result

print(solution())