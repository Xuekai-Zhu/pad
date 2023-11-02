def solution():
    james_coat = 40
    jamie_shoes = 30
    total_cost = 110

    # Subtract the cost of the coat and shoes to get the cost of the two pairs of jeans
    jeans_cost = total_cost - james_coat - jamie_shoes

    # Divide the cost of the jeans by 2 to get the cost of one pair
    one_pair_cost = jeans_cost / 2
    result = one_pair_cost
    return result

print(solution())