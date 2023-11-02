def solution():
    mitch_macarons = 20
    joshua_macarons = mitch_macarons + 6
    miles_macarons = joshua_macarons * 2
    renz_macarons = int((3/4) * miles_macarons - 1)

    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons
    kids_receiving_macarons = total_macarons // 4
    two_macarons_each = kids_receiving_macarons * 2
    result = two_macarons_each
    return result

print(solution())