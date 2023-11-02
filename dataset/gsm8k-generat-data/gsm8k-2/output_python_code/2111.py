def solution():
    """From his apartment, Kona drives 9 miles to the bakery. From there, he drives 24 miles to his grandmother’s house. From her house, he drives 27 miles straight to his apartment. How many additional miles did Kona drive round trip to the bakery stop, compared to a round trip without the bakery stop?"""
    round_trip_no_bakery = (9 + 27) * 2
    round_trip_with_bakery = ((9 + 24 + 27) * 2) - (9 * 2)
    additional_miles = round_trip_with_bakery - round_trip_no_bakery
    result = additional_miles
    return result

print(solution())