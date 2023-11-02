def solution():
    red_macaroons = 50
    green_macaroons = 40

    # Calculate the number of red macaroons Fran ate
    red_macaroons_ate = 2 * 15

    # Calculate the number of green macaroons Fran ate
    green_macaroons_ate = 15

    # Calculate the remaining number of red macaroons
    remaining_red_macaroons = red_macaroons - red_macaroons_ate

    # Calculate the remaining number of green macaroons
    remaining_green_macaroons = green_macaroons - green_macaroons_ate

    # Calculate the total number of macaroons remaining
    total_remaining_macaroons = remaining_red_macaroons + remaining_green_macaroons
    result = total_remaining_macaroons
    return result

print(solution())