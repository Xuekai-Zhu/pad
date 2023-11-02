def solution():
    """Alvin is selling his marble set. He has 100 marbles. 20% are white, 30% are black, and the rest are different colors. He sells the white ones for a nickel each, the black ones for a dime each, and the colors for $0.20 each. How much does he earn?"""
    total_marbles = 100
    white_marbles = total_marbles * 0.2
    black_marbles = total_marbles * 0.3
    colored_marbles = total_marbles - white_marbles - black_marbles

    white_earnings = white_marbles * 0.05
    black_earnings = black_marbles * 0.1
    colored_earnings = colored_marbles * 0.2

    total_earnings = white_earnings + black_earnings + colored_earnings
    result = total_earnings
    return result

print(solution())