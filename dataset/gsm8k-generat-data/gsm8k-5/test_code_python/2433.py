def solution():
    total_length = 100  # Josh has 100 feet of rope
    first_half = total_length / 2  # Josh cuts the rope in half
    second_half = first_half / 2  # Josh cuts one of the halves in half again
    fifth_piece = second_half / 5  # Josh cuts one of the remaining pieces into fifths

    # Calculate the length of the piece of rope Josh is holding
    remaining_piece = second_half - fifth_piece
    result = remaining_piece
    return result

print(solution())