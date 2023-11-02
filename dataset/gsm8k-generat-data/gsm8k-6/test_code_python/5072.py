def solution():
    # Calculate the number of butterflies left in the garden
    initial_butterflies = 9  # initial number of butterflies
    flown_away = initial_butterflies / 3  # number of butterflies that fly away
    remaining_butterflies = initial_butterflies - flown_away  # number of butterflies that are left
    result = remaining_butterflies
    return result

print(solution())