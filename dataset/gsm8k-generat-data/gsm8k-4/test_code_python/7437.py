def solution():
    """Michael and Thomas are selling their lego collections. They agree to split any money they earn. They sell them based on how many circles are on top. Each circle costs 1 cent. They earned $5 each after selling 100 single pieces, 45 double pieces, 50 triple pieces and a number of quadruple pieces. How many quadruple pieces did they sell?"""
    # Define the total number of pieces sold and the total earnings
    total_pieces = 100 + 45 + 50
    total_earnings = 10 * 100 + 20 * 45 + 30 * 50 + 500
    # 10 cents for each single piece, 20 cents for each double piece, 30 cents for each triple piece, and $5 for the quadruple pieces

    # Calculate the total cost of the circles on the quadruple pieces
    quadruple_cost = total_earnings - total_pieces
    
    # Calculate the number of circles on a quadruple piece
    quadruple_circles = 4

    # Calculate the number of quadruple pieces sold
    quadruple_pieces = quadruple_cost / (quadruple_circles * 100)

    # Return the result
    result = int(quadruple_pieces)
    return result

print(solution())