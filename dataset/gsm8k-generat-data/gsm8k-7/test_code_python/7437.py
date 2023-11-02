def solution():
    single_pieces = 100
    double_pieces = 45
    triple_pieces = 50
    total_pieces = single_pieces + (double_pieces * 2) + (triple_pieces * 3)
    total_earnings = 10  # $5 each
    earnings_per_piece = total_earnings / total_pieces

    # Calculate the number of quadruple pieces sold
    quadruple_pieces = (earnings_per_piece * 4) * x

    result = quadruple_pieces
    return result

print(solution())