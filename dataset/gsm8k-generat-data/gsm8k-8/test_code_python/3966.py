def solution():
    # Define the number of silk pieces
    silk_pieces = 10

    # Calculate the number of cashmere pieces
    cashmere_pieces = silk_pieces / 2

    # Calculate the total number of pieces
    total_pieces = 13

    # Calculate the number of pieces that use both silk and cashmere
    blend_pieces = total_pieces - silk_pieces - cashmere_pieces

    result = blend_pieces
    return result

print(solution())