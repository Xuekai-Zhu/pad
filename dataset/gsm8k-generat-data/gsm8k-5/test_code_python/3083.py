def solution():
    total_marbles = 100  # Alvin has 100 marbles
    white_marbles = total_marbles * 0.2  # 20% of the marbles are white
    black_marbles = total_marbles * 0.3  # 30% of the marbles are black
    colored_marbles = total_marbles - white_marbles - black_marbles  # The remaining marbles are colored

    # Calculate the earnings from selling white marbles
    earnings_white = white_marbles * 0.05

    # Calculate the earnings from selling black marbles
    earnings_black = black_marbles * 0.1

    # Calculate the earnings from selling colored marbles
    earnings_colored = colored_marbles * 0.2

    # Calculate the total earnings
    total_earnings = earnings_white + earnings_black + earnings_colored
    result = total_earnings
    return result

print(solution())