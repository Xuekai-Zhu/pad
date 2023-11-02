def solution():
    """Mitch made 20 macarons. Joshua made 6 more macarons than Mitch but half as many macarons as Miles. Renz made 1 fewer than 3/4 as many macarons as Miles. If they will combine their macarons to give them to the kids on the street, how many kids would receive 2 macarons each?"""
    
    # Define the number of macarons made by each person
    mitch_macarons = 20
    joshua_macarons = mitch_macarons + 6
    miles_macarons = joshua_macarons * 2
    renz_macarons = miles_macarons * 0.75 - 1

    # Calculate the total number of macarons
    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons

    # Calculate the total number of kids that can receive 2 macarons each
    total_kids = total_macarons // 4

    # return the result
    result = total_kids
    return result

print(solution())