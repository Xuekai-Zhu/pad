def solution():
    """Cindy tosses 5 dimes into the wishing pond. Eric flips 3 quarters into the pond. Garrick throws in 8 nickels. Ivy then drops 60 pennies in. If Eric dips his hands into the water and pulls out a quarter, how much money, in cents, did they put into the pond?"""
    cindy_dimes = 5
    eric_quarters = 3
    garrick_nickels = 8
    ivy_pennies = 60
    total_cents = cindy_dimes * 10 + eric_quarters * 25 + garrick_nickels * 5 + ivy_pennies
    result = total_cents
    return result

print(solution())