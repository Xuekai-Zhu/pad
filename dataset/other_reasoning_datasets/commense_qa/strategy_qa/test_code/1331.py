def solution():
    robin_hood = True
    sheriff_of_nottingham = True
    prince_john = True
    king_richard_i = True
    king_john = True

    if robin_hood and sheriff_of_nottingham and prince_john and king_richard_i and king_john:
        result = "no, some are historical figures"
    else:
        result = "yes, all are fictional"
    return result

print(solution())