def solution():
    """The total mask production was doubled every month by a company after the outbreak of Coronavirus due to increased demand. If the company produced 3000 masks in March, calculate the total mask production of July."""
    initial_production = 3000
    doubling_factor = 2
    production_in_july = initial_production * (doubling_factor ** 4)
    result = production_in_july
    return result

print(solution())