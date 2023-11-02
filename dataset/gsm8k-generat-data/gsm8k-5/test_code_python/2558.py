def solution():
    # Calculate the number of berets he can make from each color of yarn
    red_berets = 12 // 3  # James can make 4 red berets
    black_berets = 15 // 3  # James can make 5 black berets
    blue_berets = 6 // 3  # James can make 2 blue berets

    # Calculate the total number of berets he can make
    total_berets = red_berets + black_berets + blue_berets
    result = total_berets
    return result

print(solution())