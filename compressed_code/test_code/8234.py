def solution():
    
    total_marbles = 100
    white_marbles = 0.2 * total_marbles
    black_marbles = 0.3 * total_marbles
    color_marbles = total_marbles - white_marbles - black_marbles
    white_earnings = white_marbles * 0.05
    black_earnings = black_marbles * 0.1
    color_earnings = color_marbles * 0.2
    total_earnings = white_earnings + black_earnings + color_earnings
    result = total_earnings
    return result

print(solution())