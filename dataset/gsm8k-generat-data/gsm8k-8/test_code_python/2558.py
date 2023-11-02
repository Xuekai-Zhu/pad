def solution():
    # Calculate the number of berets James can make with each color
    red_berets = 12 // 3
    black_berets = 15 // 3
    blue_berets = 6 // 3

    # Determine the maximum number of berets James can make
    max_berets = min(red_berets, black_berets, blue_berets)

    result = max_berets
    return result

print(solution())