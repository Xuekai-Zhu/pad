def solution():
    """Fran baked 50 red macaroons and 40 green macarons. How many macaroons will remain if Fran ate 15 green macaroons and twice as many red macaroons as green macaroons?"""
    # Define the number of red and green macaroons baked
    red_macaroons = 50
    green_macaroons = 40

    # Define the number of green macaroons eaten and the number of red macaroons eaten
    green_eaten = 15
    red_eaten = 2 * green_eaten

    # Calculate the number of macaroons remaining
    green_remaining = green_macaroons - green_eaten
    red_remaining = red_macaroons - red_eaten
    total_remaining = green_remaining + red_remaining

    # return the result
    result = total_remaining
    return result

print(solution())