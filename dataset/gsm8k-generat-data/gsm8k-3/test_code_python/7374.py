def solution():
    """Grace baked 4 whole pumpkin pies. She sold 1 whole pumpkin pie and gave 1 whole pumpkin pie to her friend. The remaining whole pumpkin pies were each sliced into 6 pieces. Her family ate 2/3 pieces. How many pieces of pumpkin pie were left?"""
    # Define the initial number of whole pumpkin pies
    whole_pies = 4

    # Subtract the number of pies sold and given away
    whole_pies -= 2

    # Calculate the total number of pumpkin pie pieces
    total_pieces = whole_pies * 6

    # Calculate the number of pieces eaten by Grace's family
    eaten_pieces = (2/3) * total_pieces

    # Calculate the number of pieces left
    pieces_left = total_pieces - eaten_pieces

    # Display the number of pieces left
    result = pieces_left
    return result

print(solution())