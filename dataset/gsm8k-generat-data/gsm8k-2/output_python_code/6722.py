def solution():
    """The last time Bob cut his hair he cut it to 6 inches. His hair is now 36 inches long. If hair grows at a rate of .5 inches per month how many years did it take him to grow out his hair?"""
    initial_length = 6
    final_length = 36
    growth_rate = 0.5
    growth_per_month = growth_rate * 12
    total_growth = final_length - initial_length
    total_months = total_growth / growth_rate
    total_years = total_months / 12
    result = total_years
    return result

print(solution())