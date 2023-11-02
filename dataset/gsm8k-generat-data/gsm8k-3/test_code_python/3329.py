def solution():
    """Jerry is sweeping up pieces of broken glass in the parking lot. He sweeps up 20 amber pieces, 35 green pieces, and some clear pieces. If the green pieces are 25% of the total glass he sweeps up, how many pieces were clear?"""
    # Calculate the total number of glass pieces
    total_pieces = 35 / 0.25

    # Subtract the number of amber and green pieces to find the number of clear pieces
    clear_pieces = total_pieces - 20 - 35

    # Display the number of clear pieces
    result = clear_pieces
    return result

print(solution())