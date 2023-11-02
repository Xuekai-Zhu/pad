def solution():
    """Mitch made 20 macarons. Joshua made 6 more macarons than Mitch but half as many macarons as Miles. Renz made 1 fewer than 3/4 as many macarons as Miles. If they will combine their macarons to give them to the kids on the street, how many kids would receive 2 macarons each?"""
    # Define the number of macarons each person made
    mitch_macarons = 20
    joshua_macarons = mitch_macarons + 6
    miles_macarons = joshua_macarons * 2
    renz_macarons = int(0.75 * miles_macarons) - 1

    # Calculate the total number of macarons
    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons

    # Calculate the number of kids who would receive 2 macarons each
    kids = total_macarons // 4

    # Display the result
    result = kids
    return result

print(solution())