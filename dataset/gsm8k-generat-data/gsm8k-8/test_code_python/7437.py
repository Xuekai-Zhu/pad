def solution():
    # Calculate the total earnings from selling single, double and triple pieces
    total_earnings = 5 * 2
    total_earnings -= 100 # 100 single pieces
    total_earnings -= 45 * 2 # 45 double pieces
    total_earnings -= 50 * 3 # 50 triple pieces

    # Calculate the total number of circles on top of the quadruple pieces
    total_circles = total_earnings / 4

    # Calculate the number of quadruple pieces sold
    num_quadruples = total_circles / 4
    result = num_quadruples
    return result

print(solution())