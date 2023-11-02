def solution():
    # Define the initial number of macaroons
    red_macaroons = 50
    green_macaroons = 40

    # Subtract the macaroons Fran ate
    green_macaroons -= 15
    red_macaroons -= 2 * 15

    # Calculate the remaining macaroons
    remaining_macaroons = green_macaroons + red_macaroons
    result = remaining_macaroons
    return result

print(solution())