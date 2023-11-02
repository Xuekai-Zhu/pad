def solution():
    # Calculate the round trip distance without the bakery stop
    round_trip_without_bakery = 2 * 27  

    # Calculate the round trip distance with the bakery stop
    round_trip_with_bakery = 9 + 24 + 27 + 24 + 9 

    # Calculate the additional miles driven with the bakery stop
    additional_miles = round_trip_with_bakery - round_trip_without_bakery
    result = additional_miles
    return result

print(solution())