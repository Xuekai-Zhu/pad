def solution():
    """Anne drops a mirror and breaks it into 60 pieces. She sweeps up half of them, then her cat steals 3 pieces and her boyfriend picks up 1/3 of the remaining pieces. How many pieces does her boyfriend pick up?"""
    # Define the initial number of mirror pieces
    initial_pieces = 60

    # Calculate the number of pieces Anne sweeps up
    swept_pieces = initial_pieces / 2

    # Calculate the number of pieces remaining after Anne sweeps up
    remaining_pieces = initial_pieces - swept_pieces

    # Calculate the number of pieces stolen by the cat
    cat_pieces = 3

    # Calculate the number of pieces remaining after the cat steals
    remaining_pieces -= cat_pieces

    # Calculate the number of pieces picked up by Anne's boyfriend
    boyfriend_pieces = remaining_pieces / 3

    result = boyfriend_pieces
    return result

print(solution())