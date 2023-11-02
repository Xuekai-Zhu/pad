def solution():
    """Jerry is sweeping up pieces of broken glass in the parking lot. He sweeps up 20 amber pieces, 35 green pieces, and some clear pieces. If the green pieces are 25% of the total glass he sweeps up, how many pieces were clear?"""
    # Define the number of green pieces as 25% of the total
    green_pieces = 0.25 * (20 + 35 + x)

    # Solve for x, the number of clear pieces
    x = (20 + 35 + x) - green_pieces - 55

    # Return the result
    result = x
    return result

print(solution())