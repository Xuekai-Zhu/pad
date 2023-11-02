def solution():
    """Lucy lost one-third of her money. She then spent one-fourth of the remainder, and only left with $15. How much money did Lucy have at the beginning?"""
    # Let x be the amount of money Lucy had at the beginning
    # After losing one-third, she has 2/3 of her money remaining
    remaining_money1 = (2/3) * x

    # She then spends one-fourth of the remainder, leaving her with 3/4 of the remainder
    remaining_money2 = (3/4) * (remaining_money1 - (1/4) * remaining_money1)

    # At this point, she has only $15 left
    # Therefore, we can set up the following equation to solve for x:
    # remaining_money2 = 15
    (3/4) * (2/3 * x - 1/4 * 2/3 * x) = 15
    (3/4) * (1/2 * x) = 15
    (3/8) * x = 15
    x = 40

    # Therefore, Lucy had $40 at the beginning
    result = 40
    return result

print(solution())