def solution():
    
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