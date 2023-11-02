def solution():
    red_yarn = 12
    black_yarn = 15
    blue_yarn = 6

    # Calculate the total number of berets that James can make with the red yarn
    red_berets = red_yarn // 3

    # Calculate the total number of berets that James can make with the black yarn
    black_berets = black_yarn // 3

    # Calculate the total number of berets that James can make with the blue yarn
    blue_berets = blue_yarn // 3

    # Choose the lowest number of berets that can be made with any color of yarn
    total_berets = min(red_berets, black_berets, blue_berets)

    result = total_berets
    return result

print(solution())