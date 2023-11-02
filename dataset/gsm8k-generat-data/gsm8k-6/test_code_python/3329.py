def solution():
    # Calculate the total number of glass pieces Jerry sweeps up
    total_pieces = (35 / 0.25)  # green pieces are 25% of the total pieces

    # Calculate the number of clear pieces
    clear_pieces = total_pieces - 20 - 35  # subtract the number of amber and green pieces

    result = clear_pieces
    return result

print(solution())