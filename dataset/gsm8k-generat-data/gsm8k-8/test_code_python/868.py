def solution():
    # Calculate the distance from the ground to the break point
    distance_to_break = 12 / 2 - 2

    # Use the Pythagorean theorem to calculate the distance from the base
    # of the flagpole to the break point
    distance_from_base = (distance_to_break ** 2 + 6 ** 2) ** 0.5

    result = distance_from_base
    return result

print(solution())