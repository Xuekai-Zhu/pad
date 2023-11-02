def solution():
    # Calculate the number of white and brown bears
    white_bears = 60 / 2  # Christi saw twice as many black bears as white bears
    black_bears = 60
    brown_bears = black_bears + 40  # 40 more brown bears than black bears

    # Calculate the total population
    population = white_bears + black_bears + brown_bears
    result = population
    return result

print(solution())