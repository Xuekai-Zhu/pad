def solution():
    """Grace baked 4 whole pumpkin pies. She sold 1 whole pumpkin pie and gave 1 whole pumpkin pie to her friend. The remaining whole pumpkin pies were each sliced into 6 pieces. Her family ate 2/3 pieces. How many pieces of pumpkin pie were left?"""
    # Define the initial number of whole pumpkin pies
    whole_pies = 4

    # Calculate the number of whole pumpkin pies remaining after selling and giving away
    whole_pies_left = whole_pies - 2

    # Calculate the total number of pumpkin pie pieces
    total_pieces = whole_pies_left * 6

    # Calculate the number of pumpkin pie pieces eaten by her family
    family_pieces = total_pieces * (2/3)

    # Calculate the number of pumpkin pie pieces left
    pieces_left = total_pieces - family_pieces

    result = pieces_left
    return result

print(solution())