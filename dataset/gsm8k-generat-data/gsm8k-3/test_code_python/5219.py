def solution():
    """Anne drops a mirror and breaks it into 60 pieces. She sweeps up half of them, then her cat steals 3 pieces and her boyfriend picks up 1/3 of the remaining pieces. How many pieces does her boyfriend pick up?"""
    # Define the total number of pieces
    total_pieces = 60

    # Calculate the number of pieces swept up by Anne
    swept_pieces = total_pieces / 2

    # Calculate the number of pieces remaining after Anne sweeps up
    remaining_pieces = total_pieces - swept_pieces

    # Account for the pieces stolen by the cat
    remaining_pieces -= 3

    # Calculate the number of pieces picked up by Anne's boyfriend
    boyfriend_pieces = remaining_pieces / 3

    # Display the number of pieces picked up by Anne's boyfriend
    result = boyfriend_pieces
    return result

print(solution())