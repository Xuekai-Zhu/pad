def solution():
    """Jason spent 1/4 of his money and an additional $10 on some books. He then spent 2/5 of the remaining money and an additional $8 on some DVDs. If he was left with $130, how much money did he have at first?"""
    # Let x be the amount of money Jason had at first
    # After spending 1/4 of his money and $10 on books, he has (3/4)x - 10 left
    # After spending 2/5 of the remaining money and $8 on DVDs, he has (3/5)((3/4)x - 10) - 8 left
    # Setting this equal to $130, we can solve for x

    x = ((130 + 8) * (5/3)) + 10 # Solving the equation for x

    result = x
    return result

print(solution())