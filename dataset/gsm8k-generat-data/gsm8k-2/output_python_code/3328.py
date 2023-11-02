def solution():
    """Jerry is sweeping up pieces of broken glass in the parking lot. He sweeps up 20 amber pieces, 35 green pieces, and some clear pieces. If the green pieces are 25% of the total glass he sweeps up, how many pieces were clear?"""
    green_pieces = 35
    green_percent = 0.25
    total_pieces = (green_pieces / green_percent)
    amber_pieces = 20
    clear_pieces = total_pieces - green_pieces - amber_pieces
    result = clear_pieces
    return result

print(solution())