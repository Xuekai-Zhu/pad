def solution():
    """The total mask production was doubled every month by a company after the outbreak of Coronavirus due to increased demand. If the company produced 3000 masks in March, calculate the total mask production of July."""
    # Define the initial production in March
    march_production = 3000

    # Calculate the total production in July
    july_production = march_production * (2 ** 4)

    # Display the total production in July
    result = july_production
    return result

print(solution())