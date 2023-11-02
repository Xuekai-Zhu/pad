def solution():
    # Given information
    mitch_macarons = 20
    joshua_macarons = mitch_macarons + 6
    miles_macarons = joshua_macarons * 2
    renz_macarons = (3/4) * miles_macarons - 1

    # Total macarons
    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons

    # Number of kids who will receive 2 macarons each
    num_kids = total_macarons // 4

    # Number of macarons needed for the kids
    num_macarons = num_kids * 2

    result = num_kids
    return result

print(solution())