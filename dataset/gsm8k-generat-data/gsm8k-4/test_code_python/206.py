def solution():
    """There are some lions in Londolozi at first. Lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month. If there are 148 lions in Londolozi after 1 year, how many lions were there in Londolozi at first?"""
    # Define the initial number of lions and the time period in months
    initial_lions = None
    months = 12

    # Define the birth rate and death rate of lions
    birth_rate = 5
    death_rate = 1

    # Simulate the growth and decline of the lion population over the year
    lion_population = initial_lions
    for i in range(months):
        lion_population = lion_population + birth_rate - death_rate
        if lion_population > 148:
            break

    # Calculate the initial number of lions
    initial_lions = lion_population - ((birth_rate - death_rate) * (months - i))

    # Return the result
    result = initial_lions
    return result

print(solution())