def solution():
    
    mitch_macarons = 20
    josh_macarons = mitch_macarons + 6
    miles_macarons = josh_macarons * 2
    renz_macarons = int(((3/4) * miles_macarons) - 1)
    total_macarons = mitch_macarons + josh_macarons + miles_macarons + renz_macarons
    kids = total_macarons // 4
    result = kids * 2
    return result

print(solution())