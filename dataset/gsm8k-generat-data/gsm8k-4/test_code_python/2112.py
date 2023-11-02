def solution():
    """From his apartment, Kona drives 9 miles to the bakery. From there, he drives 24 miles to his grandmother’s house. From her house, he drives 27 miles straight to his apartment. How many additional miles did Kona drive round trip to the bakery stop, compared to a round trip without the bakery stop?"""
    # Calculate the total distance of the round trip without the bakery stop
    round_trip_distance_without_bakery = 27 * 2

    # Calculate the total distance of the round trip with the bakery stop
    round_trip_distance_with_bakery = 9 + 24 + 27 + 24 + 9

    # Calculate the additional distance driven with the bakery stop
    additional_distance = round_trip_distance_with_bakery - round_trip_distance_without_bakery

    result = additional_distance
    return result

print(solution())