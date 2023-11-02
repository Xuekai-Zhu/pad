def solution():
    black_bears = 60  # Given that the number of black bears in the park is 60
    white_bears = black_bears / 2  # Christi saw twice as many black bears as white bears
    brown_bears = black_bears + 40  # Christi saw 40 more brown bears than black bears

    # Calculate the population of bears in the park
    total_bears = black_bears + white_bears + brown_bears
    result = total_bears
    return result

print(solution())