def solution():
    """Cristine bought a dozen lemons and gave 1/4 of them to her neighbor. How many lemons does Cristine have left?"""
    lemons_bought = 12
    lemons_given = lemons_bought * (1/4)
    lemons_remaining = lemons_bought - lemons_given
    result = lemons_remaining
    return result

print(solution())