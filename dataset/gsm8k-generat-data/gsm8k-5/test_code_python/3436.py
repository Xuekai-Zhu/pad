def solution():
    lemons_per_dozen = 12  # There are 12 lemons in a dozen
    fraction_given_away = 1/4  # Cristine gave away 1/4 of the lemons
    lemons_bought = lemons_per_dozen  # Cristine originally bought a dozen lemons

    # Calculate the number of lemons Cristine has left
    lemons_left = lemons_bought - (fraction_given_away * lemons_bought)
    result = lemons_left
    return result

print(solution())