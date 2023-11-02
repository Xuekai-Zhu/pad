def solution():
    single_circles = 100
    double_circles = 45 * 2
    triple_circles = 50 * 3
    total_circles = single_circles + double_circles + triple_circles
    total_money = 2 * 500  # They earned $5 each, so they earned a total of $10
    remaining_money = total_money - total_circles  # The cost of the quadruple pieces is the remaining money
    quadruple_pieces = remaining_money / 4  # Each quadruple piece has 4 circles and costs 1 cent per circle
    result = quadruple_pieces
    return result

print(solution())