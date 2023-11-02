def solution():
    """From his apartment, Kona drives 9 miles to the bakery.  From there, he drives 24 miles to his grandmother’s house.  
    From her house, he drives 27 miles straight to his apartment.  How many additional miles did Kona drive round trip 
    to the bakery stop, compared to a round trip without the bakery stop?"""
    
    # Calculate the distance of a round trip from apartment to grandmother's house and back
    round_trip_distance = 2*(9+27)

    # Calculate the distance of a round trip without the bakery stop
    round_trip_without_bakery = round_trip_distance - 2*9

    # Calculate the distance of a round trip with the bakery stop
    round_trip_with_bakery = round_trip_distance + 2*9 + 2*24

    # Calculate the additional miles Kona drove round trip to the bakery stop
    additional_miles = round_trip_with_bakery - round_trip_without_bakery

    # Display the additional miles
    result = additional_miles
    return result

print(solution())