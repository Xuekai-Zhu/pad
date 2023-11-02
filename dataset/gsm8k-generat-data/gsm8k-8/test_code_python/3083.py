def solution():
    # Define the number of marbles and their percentages
    total_marbles = 100
    white_percent = 0.20
    black_percent = 0.30
    color_percent = 1 - white_percent - black_percent

    # Calculate the number of marbles of each color
    white_marbles = white_percent * total_marbles
    black_marbles = black_percent * total_marbles
    color_marbles = color_percent * total_marbles

    # Calculate the earnings from selling each color of marble
    white_earnings = white_marbles * 0.05
    black_earnings = black_marbles * 0.10
    color_earnings = color_marbles * 0.20

    # Calculate the total earnings
    total_earnings = white_earnings + black_earnings + color_earnings
    result = total_earnings
    return result

print(solution())