def solution():
    mitch_macarons = 20
    joshua_macarons = mitch_macarons + 6
    miles_macarons = joshua_macarons * 2
    renz_macarons = miles_macarons * 3/4 - 1
    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons
    kids = total_macarons / 2
    result = kids
    return result

print(solution())