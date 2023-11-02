def solution():
    # Calculate the number of white and black marbles
    white_marbles = 0.2 * 100
    black_marbles = 0.3 * 100

    # Calculate the earnings from the white, black, and different colored marbles
    earnings_white = white_marbles * 0.05
    earnings_black = black_marbles * 0.1
    earnings_colors = (100 - white_marbles - black_marbles) * 0.2

    # Calculate the total earnings
    total_earnings = earnings_white + earnings_black + earnings_colors
    result = total_earnings
    return result

print(solution())