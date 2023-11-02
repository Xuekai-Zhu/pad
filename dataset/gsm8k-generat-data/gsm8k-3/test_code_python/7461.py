def solution():
    """Christi saw twice as many black bears as white bears and 40 more brown bears than black bears in a national park. If the number of black bears in the park is 60, calculate the population of bears in the park."""
    # Calculate the number of white bears
    white_bears = 60 / 2

    # Calculate the number of black bears
    black_bears = 60

    # Calculate the number of brown bears
    brown_bears = black_bears + 40

    # Calculate the total number of bears in the park
    total_bears = white_bears + black_bears + brown_bears

    # Display the total number of bears
    result = total_bears
    return result

print(solution())