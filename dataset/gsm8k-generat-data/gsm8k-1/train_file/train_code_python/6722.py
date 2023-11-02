def solution():
    """The last time Bob cut his hair he cut it to 6 inches. His hair is now 36 inches long. If hair grows at a rate of .5 inches per month how many years did it take him to grow out his hair?"""
    initial_length = 6
    final_length = 36
    growth_rate = 0.5
    time_in_months = (final_length - initial_length) / growth_rate
    time_in_years = time_in_months / 12
    result = time_in_years
    return result

print(solution())