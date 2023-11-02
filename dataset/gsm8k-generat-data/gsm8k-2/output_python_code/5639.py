def solution():
    """Phantom's mom gave him $50 to buy printer-inks. At the store, he bought two black printer inks which cost $11 each, three red printer inks which cost $15 each, and two yellow printer inks which cost $13 each. Phantom found out that his money is not enough to buy all the printer inks. How much more money should he ask his mom to be able to buy the printer inks?"""
    total_cost = (2 * 11) + (3 * 15) + (2 * 13)
    remaining_money = 50 - total_cost
    result = abs(remaining_money)
    return result

print(solution())