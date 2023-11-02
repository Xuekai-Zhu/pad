def solution():
    
    red_macaroons = 50
    green_macaroons = 40
    eaten_green_macaroons = 15
    eaten_red_macaroons = 2 * eaten_green_macaroons
    remaining_green_macaroons = green_macaroons - eaten_green_macaroons
    remaining_red_macaroons = red_macaroons - eaten_red_macaroons
    total_remaining_macaroons = remaining_green_macaroons + remaining_red_macaroons
    result = total_remaining_macaroons
    return result

print(solution())