def solution():
    distance_without_bakery = 27 * 2  # Distance Kona would drive round trip without the bakery stop
    distance_with_bakery = (9 + 24 + 27) * 2  # Distance Kona would drive round trip with the bakery stop

    # Calculate the additional distance Kona drove round trip because of the bakery stop
    additional_distance = distance_with_bakery - distance_without_bakery
    result = additional_distance
    return result

print(solution())