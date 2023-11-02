def solution():
    """Cristine bought a dozen lemons and gave 1/4 of them to her neighbor. How many lemons does Cristine have left?"""
    lemons = 12
    given_lemons = lemons / 4
    remaining_lemons = lemons - given_lemons
    result = remaining_lemons
    return result

print(solution())