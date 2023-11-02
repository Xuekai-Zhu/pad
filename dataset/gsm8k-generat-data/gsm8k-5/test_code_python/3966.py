def solution():
    silk_pieces = 10  # Ten pieces made with silk
    cashmere_pieces = silk_pieces / 2  # Half the number of silk pieces made with cashmere
    total_pieces = 13  # Total number of pieces in the latest line
    blended_pieces = total_pieces - silk_pieces - cashmere_pieces  # Number of pieces using a blend of cashmere and silk

    result = blended_pieces
    return result

print(solution())