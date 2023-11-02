def solution():
    # Calculate the total number of circles on top of the lego pieces sold
    total_circles = 100 + (2 * 45) + (3 * 50)  # 100 single pieces, 45 double pieces, 50 triple pieces
    total_money_earned = 10  # Michael and Thomas earned $5 each

    # Calculate the total number of quadruple pieces sold and subtract their cost from the total money earned
    cost_of_quadruple_piece = 4  # each quadruple piece has 4 circles and costs 4 cents
    quadruple_pieces_sold = (total_money_earned - total_circles) // cost_of_quadruple_piece
    result = quadruple_pieces_sold
    return result

print(solution())