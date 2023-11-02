def solution():
    # First cut results in two equal halves
    first_half = 100 / 2

    # Second cut results in one half being cut into two equal pieces
    second_half = first_half / 2

    # One of the resulting pieces is cut into fifths
    final_piece = second_half / 5

    result = final_piece
    return result

print(solution())