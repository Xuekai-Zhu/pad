def solution():
    total_pieces = 60  # The chocolate bar is made up of 60 pieces
    michael_pieces = total_pieces // 2  # Michael takes half of the bar
    remaining_pieces_1 = total_pieces - michael_pieces  # Remaining pieces after Michael takes his share
    paige_pieces = remaining_pieces_1 // 2  # Paige takes half of the remaining pieces
    remaining_pieces_2 = remaining_pieces_1 - paige_pieces  # Remaining pieces after Paige takes her share
    mandy_pieces = remaining_pieces_2  # Mandy is left with the remaining pieces

    result = mandy_pieces
    return result

print(solution())