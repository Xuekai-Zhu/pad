def solution():
    """Michael and Thomas are selling their lego collections. They agree to split any money they earn. They sell them based on how many circles are on top. Each circle costs 1 cent. They earned $5 each after selling 100 single pieces, 45 double pieces, 50 triple pieces and a number of quadruple pieces. How many quadruple pieces did they sell?"""
    single_circles = 100
    double_circles = 45 * 2
    triple_circles = 50 * 3
    total_circles = single_circles + double_circles + triple_circles
    total_earned = 10  # $5 each
    total_cost = total_circles  # 1 cent per circle

    # solve for the number of quadruple pieces sold
    quadruple_circles = (total_earned - total_cost) / 4
    result = quadruple_circles

    return result

print(solution())