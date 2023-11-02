def solution():
    # Find how many macarons were made in total
    total_macarons = 20 + 6 + 2*Joshua_macarons + 4/3*Miles_macarons - 1

    # Find how many kids can receive 2 macarons each
    kids = total_macarons // 4

    result = kids
    return result

print(solution())