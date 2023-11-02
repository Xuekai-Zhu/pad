def solution():
    # Define the number of pieces Anne swept up
    swept_pieces = 60 / 2

    # Define the number of pieces left after the cat steals some
    left_pieces = swept_pieces - 3

    # Define the number of pieces her boyfriend picks up
    boyfriend_pieces = left_pieces / 3

    result = boyfriend_pieces
    return result

print(solution())