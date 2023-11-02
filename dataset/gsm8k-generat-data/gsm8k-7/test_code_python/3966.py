def solution():
    num_silk_pieces = 10
    num_cashmere_pieces = num_silk_pieces / 2
    total_pieces = 13

    # Calculate the number of pieces made with both silk and cashmere
    num_blended_pieces = total_pieces - num_silk_pieces - num_cashmere_pieces
    result = num_blended_pieces
    return result

print(solution())