def solution():
    """The total mask production was doubled every month by a company after the outbreak of Coronavirus due to increased demand. If the company produced 3000 masks in March, calculate the total mask production of July."""
    # Define the initial number of masks produced in March
    initial_production = 3000

    # Calculate the production for each month, starting from April
    april_production = initial_production * 2
    may_production = april_production * 2
    june_production = may_production * 2
    july_production = june_production * 2

    # Calculate the total production for July
    total_production = initial_production + april_production + may_production + june_production + july_production

    result = total_production
    return result

print(solution())