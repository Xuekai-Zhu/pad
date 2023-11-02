def solution():
    alis_closet_capacity = 200  # number of pairs of jeans that Ali's closet can fit
    noahs_closets_capacity = (1 / 4) * alis_closet_capacity  # capacity of one of Noah's closets
    total_capacity = 2 * noahs_closets_capacity  # total capacity of both of Noah's closets
    total_jeans = total_capacity
    return total_jeans

print(solution())