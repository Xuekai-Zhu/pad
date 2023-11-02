def solution():
    total_pieces = 13
    silk_pieces = 10
    cashmere_pieces = silk_pieces / 2
    blended_pieces = total_pieces - (silk_pieces + cashmere_pieces)
    result = blended_pieces
    return result

print(solution())