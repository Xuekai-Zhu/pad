def solution():
    """Alvin is selling his marble set. He has 100 marbles. 20% are white, 30% are black, and the rest are different colors. He sells the white ones for a nickel each, the black ones for a dime each, and the colors for $0.20 each. How much does he earn?"""
    # Define the number of marbles
    total_marbles = 100

    # Calculate the number of white and black marbles
    white_marbles = total_marbles * 0.2
    black_marbles = total_marbles * 0.3

    # Calculate the number of different colored marbles
    different_marbles = total_marbles - white_marbles - black_marbles

    # Calculate the earnings from selling white marbles
    white_earnings = white_marbles * 0.05

    # Calculate the earnings from selling black marbles
    black_earnings = black_marbles * 0.1

    # Calculate the earnings from selling different colored marbles
    different_earnings = different_marbles * 0.2

    # Calculate the total earnings
    total_earnings = white_earnings + black_earnings + different_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())