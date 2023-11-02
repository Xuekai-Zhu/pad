def solution():
    green_pieces = 35  # Jerry sweeps up 35 green pieces
    green_percentage = 0.25 # Green pieces are 25% of the total glass

    # Calculate the total number of glass pieces Jerry sweeps up
    total_pieces = (green_pieces / green_percentage)

    # Calculate the number of clear pieces
    clear_pieces = total_pieces - (amber_pieces + green_pieces)

    result = clear_pieces
    return result

print(solution())