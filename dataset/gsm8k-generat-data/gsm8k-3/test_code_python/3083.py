def solution():
    """Alvin is selling his marble set. He has 100 marbles. 20% are white, 30% are black, and the rest are different colors. He sells the white ones for a nickel each, the black ones for a dime each, and the colors for $0.20 each. How much does he earn?"""
    # Define the number of marbles and the percentages of each color
    total_marbles = 100
    white_percentage = 0.20
    black_percentage = 0.30

    # Calculate the number of each color of marble
    white_marbles = int(total_marbles * white_percentage)
    black_marbles = int(total_marbles * black_percentage)
    color_marbles = total_marbles - white_marbles - black_marbles

    # Calculate the earnings from the sale of each color of marble
    white_earnings = white_marbles * 0.05
    black_earnings = black_marbles * 0.10
    color_earnings = color_marbles * 0.20

    # Calculate the total earnings
    total_earnings = white_earnings + black_earnings + color_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())