def solution():
    """Frank spent 1/5 of his money to buy groceries. He then spent 1/4 of the remaining money to buy a magazine. If he had $360 left in his wallet, how much money did he have at first?"""
    # Let x be the amount of money Frank had at first
    # He spent 1/5 of his money on groceries, so he has 4/5 of his money remaining
    remaining_money1 = x * (4/5)
    # He spent 1/4 of this remaining money on a magazine, so he has 3/4 of it remaining
    remaining_money2 = remaining_money1 * (3/4)
    # If he has $360 left, then 3/4 of his remaining money is $360
    remaining_money2 = 360 / (3/4)
    # Solve for x
    x = remaining_money2 / (4/5)
    # Display the original amount of money Frank had
    result = x
    return result

print(solution())