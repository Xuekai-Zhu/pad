def solution():
    distance_to_bakery = 9
    distance_to_grandmother = 24
    distance_from_grandmother = 27

    # Calculate the total distance of a round trip without the bakery stop
    round_trip_distance = 2 * (distance_to_grandmother + distance_from_grandmother)

    # Calculate the total distance of a round trip with the bakery stop
    round_trip_with_bakery = 2 * (distance_to_bakery + distance_to_grandmother + distance_from_grandmother)

    # Calculate the additional distance driven due to the bakery stop
    additional_distance = round_trip_with_bakery - round_trip_distance
    result = additional_distance
    return result

print(solution())