def solution():
    # Height of the flagpole before it broke
    initial_height = 12

    # Length of the remaining part of the flagpole after the break
    remaining_height = initial_height / 2

    # Distance from the base to the point where the flagpole broke
    distance_from_base = ((initial_height - remaining_height) ** 2 - 2 ** 2) ** 0.5
    result = distance_from_base
    return result

print(solution())