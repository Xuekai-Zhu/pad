def solution():
    """Fran baked 50 red macaroons and 40 green macarons. How many macaroons will remain if Fran ate 15 green macaroons and twice as many red macaroons as green macaroons?"""
    # Define the initial number of red and green macaroons
    red_macaroons = 50
    green_macaroons = 40

    # Fran eats some macaroons
    green_macaroons -= 15
    red_macaroons -= 2*green_macaroons

    # Calculate the total number of macaroons remaining
    total_macaroons = red_macaroons + green_macaroons

    # Display the total number of macaroons remaining
    result = total_macaroons
    return result

print(solution())