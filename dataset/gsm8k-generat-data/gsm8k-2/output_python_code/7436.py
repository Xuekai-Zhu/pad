def solution():
    """Michael and Thomas are selling their lego collections. They agree to split any money they earn. They sell them based on how many circles are on top. Each circle costs 1 cent. They earned $5 each after selling 100 single pieces, 45 double pieces, 50 triple pieces and a number of quadruple pieces. How many quadruple pieces did they sell?"""
    single_circles = 1
    double_circles = 2
    triple_circles = 3
    total_single_pieces = 100
    total_double_pieces = 45
    total_triple_pieces = 50
    total_money_earned = 1000  # in cents, $10
    total_circles = (total_single_pieces * single_circles) + (total_double_pieces * double_circles) + (
                total_triple_pieces * triple_circles)
    quadruple_circles = (total_money_earned - total_circles) / 4
    result = quadruple_circles
    return result

print(solution())