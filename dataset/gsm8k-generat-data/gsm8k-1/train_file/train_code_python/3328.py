def solution():
    """Jerry is sweeping up pieces of broken glass in the parking lot. He sweeps up 20 amber pieces, 35 green pieces, and some clear pieces. If the green pieces are 25% of the total glass he sweeps up, how many pieces were clear?"""
    green_pieces = 35
    green_percent = 25
    total_percent = 100
    total_pieces = (green_pieces * total_percent) / green_percent
    clear_pieces = total_pieces - (green_pieces + 20)
    result = clear_pieces
    return result

print(solution())