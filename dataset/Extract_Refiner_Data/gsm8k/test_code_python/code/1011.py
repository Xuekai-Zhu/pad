def solution():
    
    # Define the number of packs and pieces per pack
    PACKS = 15
    pieces_per_pack = 60

    # Calculate the total number of pieces of sweets
    total_pieces = PACKS * pieces_per_pack

    # Calculate the number of pieces of sweets Anne kept
    kept_pieces = 2 * pieces_per_pack

    # Calculate the number of pieces of sweets given to her friends
    given_pieces = total_pieces - kept_pieces

    # Calculate the number of pieces of sweets each friend received
    friend_pieces = given_pieces / 10

    # Display the number of pieces of sweets each friend received
    result = friend_pieces
    return result

print(solution())