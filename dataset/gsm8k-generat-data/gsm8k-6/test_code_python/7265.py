def solution():
    # Calculate the number of pieces of chocolate Mandy will get
    michael_pieces = 60 / 2  # Michael takes half of the bar
    remaining_pieces = 60 - michael_pieces  # Calculate the remaining pieces of chocolate
    paige_pieces = remaining_pieces / 2  # Paige takes half of the remainder
    mandy_pieces = remaining_pieces - paige_pieces  # Mandy is left with what's left of the chocolate bar
    result = mandy_pieces
    return result

print(solution())