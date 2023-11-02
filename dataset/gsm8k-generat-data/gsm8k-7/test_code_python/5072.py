def solution():
    initial_butterflies = 9
    fraction_flied_away = 1/3

    # Calculate the number of butterflies that flew away
    butterflies_flied_away = initial_butterflies * fraction_flied_away

    # Calculate the number of butterflies left in the garden
    remaining_butterflies = initial_butterflies - butterflies_flied_away
    result = remaining_butterflies
    return result

print(solution())