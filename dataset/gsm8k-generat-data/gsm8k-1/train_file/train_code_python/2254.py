def solution():
    """Mitch made 20 macarons. Joshua made 6 more macarons than Mitch but half as many macarons as Miles. Renz made 1 fewer than 3/4 as many macarons as Miles. If they will combine their macarons to give them to the kids on the street, how many kids would receive 2 macarons each?"""
    mitch_macarons = 20
    josh_macarons = mitch_macarons + 6
    miles_macarons = josh_macarons * 2
    renz_macarons = int(((3/4) * miles_macarons) - 1)
    total_macarons = mitch_macarons + josh_macarons + miles_macarons + renz_macarons
    kids = total_macarons // 4
    result = kids * 2
    return result

print(solution())