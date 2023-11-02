def solution():
    # Calculate the total length needed in feet
    total_length = 6 * 10

    # Calculate the length of each piece of rope after losing 25%
    piece_length = 0.75 * 20

    # Calculate the number of pieces needed
    num_pieces = total_length // piece_length

    # If there is a remainder, add an extra piece
    if total_length % piece_length != 0:
        num_pieces += 1

    result = num_pieces
    return result

print(solution())