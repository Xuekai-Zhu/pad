def solution():
    # Define the number of black bears
    black_bears = 60

    # Calculate the number of white bears
    white_bears = black_bears / 2

    # Calculate the number of brown bears
    brown_bears = black_bears + 40

    # Calculate the total population of bears
    total_population = black_bears + white_bears + brown_bears
    result = total_population
    return result

print(solution())