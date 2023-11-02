def solution():
    # Calculate the total growth of the plant in a year
    total_growth = 80 - 20  # the plant reaches a height of 80 feet after a year and is currently 20 feet tall

    # Calculate the monthly growth rate
    monthly_growth_rate = total_growth / 12  # the plant grows at the same rate each month

    result = monthly_growth_rate
    return result

print(solution())