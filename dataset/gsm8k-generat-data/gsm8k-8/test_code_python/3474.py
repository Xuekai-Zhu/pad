def solution():
    # Convert hourly wage to cents per second
    wage_per_second = 10 * 100 / 3600

    # Calculate how many weeds Heather needs to pick per second to earn the wage
    weeds_per_second = wage_per_second / 0.05

    result = round(1/weeds_per_second, 2)
    return result

print(solution())