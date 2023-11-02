def solution():
    mitch_macarons = 20  # Mitch made 20 macarons
    joshua_macarons = mitch_macarons + 6  # Joshua made 6 more macarons than Mitch
    miles_macarons = joshua_macarons * 2  # Miles made twice as many macarons as Joshua
    renz_macarons = int((3/4) * miles_macarons) - 1  # Renz made 1 fewer than 3/4 as many macarons as Miles
    
    # Combine all the macarons made by the four people
    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons
    
    # Calculate how many kids would receive 2 macarons each
    kids = int(total_macarons / 4)  # Each kid will receive 2 macarons
    result = kids
    return result

print(solution())