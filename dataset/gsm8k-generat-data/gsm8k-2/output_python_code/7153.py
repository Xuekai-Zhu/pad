def solution():
    """Isabella and Alexis went to the mall to buy some pants and dresses. Alexis bought 3 times more pants and dresses than Isabella. If Alexis bought 21 pairs of pants and 18 dresses, how many pairs of pants and dresses did Isabella buy in total?"""
    alexis_pants = 3 * isabella_pants
    alexis_dresses = 3 * isabella_dresses
    total_pants = isabella_pants + alexis_pants
    total_dresses = isabella_dresses + alexis_dresses

    # set up equations using the given information
    # 21 = 4*A + 3*B
    # 18 = A + 2*B
    A = (21 - 3*18) / (4 - 3*2)
    B = (18 - A) / 2

    result = total_pants + total_dresses
    return result

print(solution())