def solution():
    # Calculate the round trip distance without the bakery stop
    round_trip_distance_without_bakery = 2 * 27

    # Calculate the round trip distance with the bakery stop
    round_trip_distance_with_bakery = 9 + 24 + 9 + 24

    # Calculate the additional miles driven due to the bakery stop
    additional_miles_driven = round_trip_distance_with_bakery - round_trip_distance_without_bakery

    result = additional_miles_driven
    return result

print(solution())