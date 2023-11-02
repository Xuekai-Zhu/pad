def solution():
    """Christi saw twice as many black bears as white bears and 40 more brown bears than black bears in a national park.
    If the number of black bears in the park is 60, calculate the population of bears in the park."""
    black_bears = 60
    white_bears = black_bears / 2
    brown_bears = black_bears + 40
    total_bears = black_bears + white_bears + brown_bears
    result = total_bears
    return result

print(solution())