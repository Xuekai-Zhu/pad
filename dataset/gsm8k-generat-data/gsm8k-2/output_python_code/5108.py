def solution():
    """The total mask production was doubled every month by a company after the outbreak of Coronavirus due to increased demand. If the company produced 3000 masks in March, calculate the total mask production of July."""
    march_production = 3000
    total_production = march_production * 2 ** 4  # 4 months from March to July
    result = total_production
    return result

print(solution())