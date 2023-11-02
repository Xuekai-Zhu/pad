def solution():
    # Initial quantities
    red_macaroons = 50
    green_macaroons = 40

    # Subtracting the macaroons Fran ate
    green_macaroons -= 15
    red_macaroons -= 2 * 15

    # Total number of macaroons remaining
    remaining_macaroons = red_macaroons + green_macaroons
    result = remaining_macaroons
    return result

print(solution())