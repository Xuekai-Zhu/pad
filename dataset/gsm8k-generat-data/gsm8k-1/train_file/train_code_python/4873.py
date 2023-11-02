def solution():
    """Fran baked 50 red macaroons and 40 green macarons. How many macaroons will remain if Fran ate 15 green macaroons and twice as many red macaroons as green macaroons?"""
    red_macaroons = 50
    green_macaroons = 40
    green_macaroons_eaten = 15
    red_macaroons_eaten = 2 * green_macaroons_eaten
    remaining_red_macaroons = red_macaroons - red_macaroons_eaten
    remaining_green_macaroons = green_macaroons - green_macaroons_eaten
    total_macaroons_remaining = remaining_green_macaroons + remaining_red_macaroons
    result = total_macaroons_remaining
    return result

print(solution())