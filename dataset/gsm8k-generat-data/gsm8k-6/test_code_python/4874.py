def solution():
    # Calculate the number of remaining macaroons
    remaining_red = 50 - 2*15  # Fran ate twice as many red macaroons as green macaroons
    remaining_green = 40 - 15
    total_remaining = remaining_red + remaining_green
    result = total_remaining
    return result

print(solution())