def solution():
    """Ravi has some coins. He has 2 more quarters than nickels and 4 more dimes than quarters. If he has 6 nickels, how much money does he have?"""
    nickels = 6
    quarters = nickels + 2
    dimes = quarters + 4
    total = (nickels * 0.05) + (quarters * 0.25) + (dimes * 0.1)
    result = total
    return result

print(solution())