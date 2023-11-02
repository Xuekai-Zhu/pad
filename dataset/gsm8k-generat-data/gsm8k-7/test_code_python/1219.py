def solution():
    pasta_order = 6
    pasta_pieces = 2

    bbq_order = 3
    bbq_pieces = 3

    fried_order = 2
    fried_pieces = 8

    # calculate total pieces of chicken for pasta orders
    total_pasta = pasta_order * pasta_pieces

    # calculate total pieces of chicken for bbq orders
    total_bbq = bbq_order * bbq_pieces

    # calculate total pieces of chicken for fried orders
    total_fried = fried_order * fried_pieces

    # calculate total pieces of chicken needed for all orders
    total_chicken = total_pasta + total_bbq + total_fried

    result = total_chicken
    return result

print(solution())